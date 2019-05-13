#!/usr/bin/env python3

import os
import json
import click
from requests import Session
from zeep import Transport, Client, Settings
from zeep.helpers import serialize_object
from zeep.cache import SqliteCache
from datetime import datetime
from subprocess import run
from functools import singledispatch, wraps

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
            transport = Transport(session=Session(), cache=SqliteCache())
            settings = Settings(strict=False)
            self.clients[endpoint] = Client(wsdl,
                                            transport=transport,
                                            service_name=endpoint,
                                            settings=settings
                                            )

        return self.clients[endpoint]

    def auth_transport(self, transport):

        auth_wsdl = "https://{}/Panopto/PublicAPI/4.2/Auth.svc".format(self.host)
        auth_client = Client(auth_wsdl + "?singleWsdl", transport=transport)
        auth_service = auth_client.create_service(
            binding_name=AUTH_BINDING, address=auth_wsdl)
        with auth_client.settings(raw_response=True):
            auth_service.LogOnWithPassword(self.user, self.password)


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

        options = generate_options(operation.input.body.type.elements)

        @ctx.command.command(name=cmd_name)
        @click.pass_context
        def _cmd(ctx, *args, **kwargs):

            # set the auth cookie for our client transport
            ctx.obj.auth_transport(client.transport)

            # click nicely lowercases all our option names, so we have
            # to re-camelcase them here
            op_params = camelcase_params(options, kwargs)

            op = getattr(client.service, cmd_name)
            try:
                res = op(**op_params)
            except Exception as e:
                print(e)
                ctx.exit(1)
            res = serialize_object(res)
            print(json.dumps(res, indent=True, default=to_serializable))

        apply_generated_options(_cmd, options)
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


def generate_options(elements):
    options = {}
    for name, elem in elements:

        if name == "auth": # auth is handled by client instantiation
            continue

        type_name = elem.type.name
        make_option_kwargs = {}

        if elem.type._element is not None:
            if type_name.startswith('ArrayOf'):
                make_option_kwargs["multiple"] = True
                make_option_kwargs["help"] = "allows multiple"
            else:
                options[name] = generate_options(elem.type._element.elements)
                continue

        if type_name in OPTION_CHOICES:
            choice = click.Choice(OPTION_CHOICES[type_name])
            options[name] = make_option(name, choice, **make_option_kwargs)
        elif type_name == "dateTime":
            options[name] = make_option(name, click.DateTime(), **make_option_kwargs)
        elif type_name == 'int':
            options[name] = make_option(name, click.INT, **make_option_kwargs)
        elif type_name == 'double':
            options[name] = make_option(name, click.FLOAT, **make_option_kwargs)
        elif type_name == 'boolean':
            make_option_kwargs["help"] = "true|false"
            options[name] = make_option(name, click.BOOL, **make_option_kwargs)
        else:
            options[name] = make_option(name, click.STRING, **make_option_kwargs)
    return options


def make_option(name, option_type, **kwargs):
    param_decls = "--{}".format(name)
    return click.option(param_decls, type=option_type, **kwargs)


def camelcase_params(options, command_kwargs):
    params = {}
    for param_name, option in options.items():
        if isinstance(option, dict):
            params[param_name] = camelcase_params(option, command_kwargs)
        else:
            params[param_name] = command_kwargs[param_name.lower()]
    return params


def apply_generated_options(cmd, options):
    for _, option in options.items():
        if isinstance(option, dict):
            apply_generated_options(cmd, option)
        else:
            cmd = option(cmd)


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

OPTION_CHOICES = {
    'UsageGranularity': [
        'Hourly',
        'Daily',
        'Weekly'
    ],
    'StatsReportType': [
        'FolderUsage',
        'SessionUsage',
        'UserViewingUsage',
        'UserCreationUsage',
        'LastLoginTime',
        'SessionsViewsByUsers',
        'SessionsViewsByViewingType',
        'SessionsCreatedOrEdited',
        'RemoteRecorderUsage',
        'SystemViews',
    ],
    'AccessRole': [
        'Creator',
        'Viewer',
        'ViewerWithLink',
        'Publisher'
    ],
    'SystemRole': [
        'None',
        'Videographer',
        'Admin'
    ],
    'RecorderSortField': [
        'Name',
        'State'
    ],
    'ArrayOfDayOfWeek': [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ],
    'SessionSortField': [
        'Name',
        'Date',
        'Duration',
        'State',
        'Relevance',
        'Order'
    ],
    'FolderSortField': [
        'Name',
        'Sessions',
        'Relavance'
    ],
    'UserSortField': [
        'UserKey',
        'Role',
        'Added',
        'LastLogOn',
        'Email',
        'FullName'
    ],
    'FolderStartSettingType': [
        'Immediately',
        'WhenPublisherApproved',
        'NeverUnlessSessionSet',
        'SpecificDate'
    ],
    'SessionStartSettingType': [
        'Immediately',
        'WithItsFolder',
        'SpecificDate'
    ],
    'SessionEndSettingType': [
        'Forever',
        'WithItsFolder',
        'SpecificDate'
    ]
}


for name, ver in ENDPOINTS.items():

    @cli.command(name=name, cls=EndpointGroup)
    @click.pass_context
    def _subgroup(ctx):
        pass


@cli.command(hidden=True)
@click.pass_context
def generate_usage(ctx):

    content = ""
    toc = ""

    cmd = create_usage_command([])
    res = run(cmd, capture_output=True)
    content += get_usage('', 2, res.stdout.decode())

    for command_group, command in cli.commands.items():
        if command_group == 'generate-usage':
            continue
        cmd = create_usage_command([command_group])
        res = run(cmd, capture_output=True)
        content += get_usage(command_group, 3, res.stdout.decode())
        toc += create_toc_entry([command_group])

        client = ctx.obj.get_client(command_group)
        service = client.wsdl.services[command_group]
        port = service.ports["BasicHttpBinding_I" + command_group]
        for op_name in port.binding._operations.keys():
            cmd = create_usage_command([command_group, op_name])
            res = run(cmd, capture_output=True)
            content += get_usage(" ".join((command_group, op_name)), 5, res.stdout.decode())
            toc += create_toc_entry([command_group, op_name], subcommand=True)

    print(toc + "\n\n")
    print(content)

def create_usage_command(commands):
    return ["python", __file__] + commands + ["--help"]

def create_toc_entry(commands, subcommand=False):
    return "{}* [{}](#panopto-{})\n".format(
        subcommand and "\t" or "",
        subcommand and commands[1] or " ".join(commands),
        "-".join(commands)
    )

def get_usage(header, header_size, usage):
    return """
{} panopto {}
```
{}
```
""".format("#" * header_size, header, usage)


if __name__ == '__main__':
    cli()
