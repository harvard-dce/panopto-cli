#!/usr/bin/env python3

import os
import json
import click
from requests import Session
from zeep import Transport, Client
from zeep.helpers import serialize_object
from datetime import datetime
from functools import singledispatch

# supress warnings about forced https
import logging
logging.getLogger("zeep.wsdl.bindings.soap").setLevel(logging.ERROR)

AUTH_URL = 'https://{host}/Panopto/PublicAPI/4.2/Auth.svc'
AUTH_BINDING = '{http://tempuri.org/}BasicHttpBinding_IAuth'


def load_config():
    config_file = os.path.expanduser('~/.panopto-cli')
    if os.path.exists(config_file):
        with open(config_file) as f:
            config = json.load(f)
        return config
    return {}


# handle serializing datetimes in json
@singledispatch
def to_serializable(val):
    return str(val)

@to_serializable.register(datetime)
def ts_datetime(val):
    return val.isoformat() + "Z"


class PanoptoAPI(object):

    def __init__(self, user, password, host):

        self.user = user
        self.password = password
        self.host = host
        self.clients = {}

    def get_client(self, endpoint):

        if endpoint not in self.clients:
            wsdl = "https://{}/Panopto/PublicAPI/{}/{}.svc?singleWsdl".format(
                self.host, ENDPOINTS[endpoint], endpoint
            )
            transport = Transport(session=Session())
            self.clients[endpoint] = Client(wsdl, transport=transport, service_name=endpoint)

        return self.clients[endpoint]

    def auth_transport(self, transport):

        auth_wsdl = "https://{}/Panopto/PublicAPI/4.2/Auth.svc".format(self.host)
        auth_client = Client(auth_wsdl + "?singleWsdl", transport=transport)
        auth_service = auth_client.create_service(
            binding_name=AUTH_BINDING, address=auth_wsdl)
        with auth_client.settings(raw_response=True):
            resp = auth_service.LogOnWithPassword(self.user, self.password)


class EndpointGroup(click.Group):

    def get_command(self, ctx, cmd_name):

        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv

        client = ctx.obj.get_client(ctx.info_name)

        try:
            service = client.wsdl.services[ctx.info_name]
            port = service.ports["BasicHttpBinding_I" + ctx.info_name]
            operation = port.binding._operations[cmd_name]
        except KeyError as e:
            ctx.fail('command {} not found: {}'.format(cmd_name, e))

        options = self.generate_options(operation)

        @ctx.command.command(name=cmd_name)
        @click.pass_context
        def _cmd(ctx, *args, **kwargs):

            # set the auth cookie for our client transport
            ctx.obj.auth_transport(client.transport)

            # click nicely lowercases all our option names, so we have
            # to re-camelcase them here
            camel_case_params = {}
            for param_name, option in options.items():
                if isinstance(option, dict):
                    camel_case_params[param_name] = {
                        x: kwargs[x.lower()] for x in option.keys()
                    }
                else:
                    camel_case_params[param_name] = kwargs[param_name.lower()]

            op = getattr(client.service, cmd_name)
            try:
                res = op(**camel_case_params)
            except Exception as e:
                print(e)
                ctx.exit(1)
            res = serialize_object(res)
            print(json.dumps(res, indent=True, default=to_serializable))

        for option in options.values():
            if isinstance(option, dict):
                for sub_option in option.values():
                    _cmd = sub_option(_cmd)
            else:
                _cmd = option(_cmd)

        return _cmd

    def list_commands(self, ctx):
        client = ctx.obj.get_client(ctx.info_name)
        commands = []
        # should be only one service/port combo per wsdl
        for service in client.wsdl.services.values():
            for port in service.ports.values():
                for op in port.binding._operations.values():
                    commands.append(op.name)
        return commands


    def generate_options(self, operation):

        options = {}

        for name, elem in operation.input.body.type.elements:
            if name == "auth": continue

            if elem.type.name == "dateTime":
                options[name] = self.make_option(name, click.DateTime())
            elif name == "pagination":
                options["pagination"] = {
                    "PageNumber": self.make_option("PageNumber", int,
                                                   default=1),
                    "MaxNumberResults": self.make_option("MaxNumberResults",
                                                         int, default=10)
                }
            else:
                options[name] = self.make_option(name, str)

        return options

    def make_option(self, name, option_type, **kwargs):
        param_decls = "--{}".format(name)
        return click.option(param_decls, type=option_type, **kwargs)




@click.group()
@click.option('--user')
@click.option('--password')
@click.option('--host')
@click.pass_context
def cli(ctx, user, password, host):
    config = load_config()
    user = user or config.get('user')
    password = password or config.get('password')
    host = host or config.get('host')
    if any(x is None for x in (host, user, password)):
        ctx.fail("Missing configuration: host, user or password is missing")
    ctx.obj = PanoptoAPI(user, password, host)
    return


ENDPOINTS = {
    'AccessManagement': '4.0',
    'RemoteRecorderManagement': '4.2',
    'SessionManagement': '4.6',
    'UsageReporting': '4.0',
    'UserManagement': '4.0'
}

for name, ver in ENDPOINTS.items():

    @cli.command(name=name, cls=EndpointGroup)
    @click.pass_context
    def _subgroup(ctx):
        pass


if __name__ == '__main__':
    cli()
