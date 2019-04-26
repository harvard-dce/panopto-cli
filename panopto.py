#!/usr/bin/env python3

import json
import click
import arrow
from pprint import pprint
from requests import Session
from dotenv import load_dotenv
from zeep import Transport, Client
from zeep.helpers import serialize_object

# supress warnings about forced https
import logging
logging.getLogger("zeep.wsdl.bindings.soap").setLevel(logging.ERROR)

load_dotenv()

AUTH_URL = 'https://{host}/Panopto/PublicAPI/4.2/Auth.svc'
AUTH_BINDING = '{http://tempuri.org/}BasicHttpBinding_IAuth'

class PanoptoAPI(object):

    def __init__(self, user, password, host):

        transport = Transport(session=Session())
        auth_wsdl = "https://{}/Panopto/PublicAPI/4.2/Auth.svc".format(host)
        auth_client = Client(auth_wsdl + "?singleWsdl", transport=transport)
        auth_service = auth_client.create_service(
            binding_name=AUTH_BINDING, address=auth_wsdl)
        with auth_client.settings(raw_response=True):
            resp = auth_service.LogOnWithPassword(user, password)

        self.transport = transport
        self.host = host

    def get_client(self, endpoint):

        wsdl = "https://{}/Panopto/PublicAPI/{}/{}.svc?singleWsdl".format(
            self.host, ENDPOINTS[endpoint], endpoint
        )
        return Client(wsdl, transport=self.transport, service_name=endpoint)


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

        options = {
            name: self.generate_option(x)
            for name, x in operation.input.body.type.elements
            if name != "auth" # auth is handled by the transport
        }

        @ctx.command.command(name=cmd_name)
        @click.pass_context
        def _cmd(ctx, *args, **kwargs):

            # click nicely lowercases all our option names, so we have
            # to re-camelcase them here
            camel_case_params = {}
            for param_name in options.keys():
                camel_case_params[param_name] = kwargs[param_name.lower()]

            op = getattr(client.service, cmd_name)
            res = op(**camel_case_params)
            #print(json.dumps(res, indent=True))
            res = serialize_object(res)
            print(res)

        for option in options.values():
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


    def generate_option(self, element):

        param_decls = "--{}".format(element.name)
        if element.type.name == "dateTime":
            option_type = click.DateTime()
        else:
            option_type = str
        option = click.option(param_decls, type=option_type)

        return option


@click.group()
@click.option('--user', envvar="PANOPTO_USER")
@click.option('--password', envvar="PANOPTO_PASSWORD")
@click.option('--host', envvar="PANOPTO_HOST")
@click.pass_context
def cli(ctx, user, password, host):
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
