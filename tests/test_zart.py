#!/usr/bin/env python3

import click
from click.testing import CliRunner
from zart import cli

def test_noargs(runner):
    click.secho('test - no args: ', fg='green')
    result = runner.invoke(cli)
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)
    assert 'Usage:' in result.output
    assert 'Options:' in result.output

def test_command(runner, command):
    click.secho('test command - ' + command, fg='green')
    result = runner.invoke(cli, [command])
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)

def test_command_flag(runner, command, flag):
    flag = '--' + flag
    click.secho('test command - help: ' + command + ' ' + flag, fg='green')
    result = runner.invoke(cli, [command, flag])
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)
    assert command in result.output
    assert 'Usage:' in result.output
    assert 'Options:' in result.output

def test_command_comm(runner, command, flag):
    flag = '--' + flag
    click.secho('test command comm: ' + command + ' ' + flag, fg='green')
    if command == 'graphitem':
        if flag == '--startSearch':
            click.secho('graphitem: does not have this option', fg='yellow')
            return
    if command == 'trend':
        if flag == '--editable' or flag == '--preservekeys' or flag == '--startSearch':
            click.secho('trend: does not have this option', fg='yellow')
            return
    result = runner.invoke(cli, [command, flag])
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)

def test_command_comm_ints(runner, command, flag):
    flag = '--' + flag
    click.secho('test_command_comm_ints: ' + command + ' ' + flag + ' 1', fg='green')
    result = runner.invoke(cli, [command, flag, 1])
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)

def test_method_ids(runner, method, flag):
    flag = '--' + flag
    click.secho('test_method_ids: ' + method + ' ' + flag, fg='green')
    result = runner.invoke(cli, [method, flag, 1])
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)

def test_method_bool(runner, method, flag):
    flag = '--' + flag
    click.secho('test_method_bool: ' + method + ' ' + flag, fg='green')
    result = runner.invoke(cli, [method, flag])
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)

def test_method_flag(runner, method, flag):
    flag = '--' + flag
    click.secho('test_method_flag: ' + method + ' ' + flag, fg='green')
    result = runner.invoke(cli, [method, flag])
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)

def test_method_sort(runner, method, flag, value):
    flag = '--' + flag
    click.secho('test_method_sort: ' + method + ' ' + flag + ' ' + value, fg='green')
    result = runner.invoke(cli, [method, flag, value])
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)

def test_method_times(runner, method, flag):
    flag = '--' + flag
    click.secho('test_method_times: ' + method + ' ' + flag, fg='green')
    result = runner.invoke(cli, [method, flag, 1])
    assert result.exit_code == 0, 'exitcode: ' + str(result.exit_code)


def test_prog_noargs(runner):
    click.secho('test_prog_noargs', fg='green')
    result = runner.invoke(cli)
    click.secho(str(result.exit_code), fg='yellow')
    assert result.exit_code == 0
    assert 'Usage:' in result.output
    assert 'Options:' in result.output
    assert 'Commands:' in result.output
    assert 'Error: Missing command.' not in result.output
    assert 'Error: No such command' not in result.output
    assert 'Error: no such option' not in result.output

def test_prog_version(runner):
    click.secho('test_prog_version', fg='green')
    result = runner.invoke(cli, '--version')
    click.secho(str(result.exit_code), fg='yellow')
    assert result.exit_code == 0
    assert 'Error: Missing command.' not in result.output
    assert 'Error: No such command' not in result.output
    assert 'Error: no such option' not in result.output

def test_prog_help(runner):
    click.secho('test_prog_help', fg='green')
    result = runner.invoke(cli, '--help')
    click.secho(str(result.exit_code), fg='yellow')
    assert result.exit_code == 0
    assert 'Usage:' in result.output
    assert 'Options:' in result.output
    assert 'Commands:' in result.output
    assert 'Error: Missing command.' not in result.output
    assert 'Error: No such command' not in result.output
    assert 'Error: no such option' not in result.output

def test_bad_option(runner):
    click.secho('test_bad_option', fg='green')
    result = runner.invoke(cli, '--badflag')
    click.secho(str(result.exit_code), fg='yellow')
    click.secho(result.output, fg='red')
    assert result.exit_code == 2
    assert 'Usage: zart.py [OPTIONS] COMMAND [ARGS]...' in result.output
    assert 'Error: Missing command.' not in result.output
    assert 'Error: No such command' not in result.output
    assert 'Error: no such option' in result.output

def test_bad_method(runner):
    click.secho('test_bad_method', fg='green')
    result = runner.invoke(cli, 'badmethod')
    click.secho(result.exit_code, fg='yellow')
    assert result.exit_code == 2
    assert 'Usage: zart.py [OPTIONS] COMMAND [ARGS]...' in result.output
    assert 'Error: No such command' in result.output
    assert 'Error: no such option' not in result.output

def test_method_noflag(runner, method):
    result = runner.invoke(cli, method)
    click.secho(result.exit_code, fg='yellow')
    assert result.exit_code == 0
    assert 'Usage: zart.py [OPTIONS] COMMAND [ARGS]...' not in result.output
    assert 'Error: no such option' not in result.output
    assert 'Error: No such command' not in result.output


def test_version(runner, flag, exitcode):
    click.secho('test_version: ' + PROG + ' ' + flag, fg='green')
    result = runner.invoke(cli, [flag])
    assert result.exit_code == exitcode
    assert 'version' in result.output

def test_basic_help(runner, flag, exitcode):
    click.secho('test_basic_help: ' + PROG + ' ' + flag, fg='green')
    result = runner.invoke(cli, [flag])
    assert result.exit_code == exitcode

def test_basic_missing_args(runner, flag, exitcode):
    click.secho('test_basic_missing_args: ' + PROG + ' ' + flag, fg='green')
    result = runner.invoke(cli, [flag])
    assert result.exit_code == exitcode
    assert result.output == 'Error: ' + flag + ' option requires an argument\n'


def test_method_option(runner, method, flag, option, exitcode):
    click.secho('test_method_option: ' + PROG + ' ' + method + ' ' + flag + ' ' + str(option), fg='green')
    result = runner.invoke(cli, [method, flag, option])
    assert result.exit_code == exitcode

def test_method_countoutput(runner, method, flag, exitcode):
    click.secho('test_method_countoutput: ' + PROG + ' ' + method + ' ' + flag, fg='green')
    result = runner.invoke(cli, [method, flag])
    assert result.exit_code == exitcode
#    assert result.output == str(count) + '\n'
    assert type(result.output) is IntType, "result is not an integer: %r" % result.output

def main():

    commands=(
        'action',
        'alert',
        'application',
        'autoregistration',
        'correlation',
        'dashboard',
        'dcheck',
        'dhost',
        'drule',
        'dservice',
        'event',
        'graph',
        'graphitem',
        'graphprototype',
        'history',
        'host',
        'hostgroup',
        'hostinterface',
        'hostprototype',
        'httptest',
        'iconmap',
        'image',
        'item',
        'itemprototype',
        'maintenance',
        'map',
        'mediatype',
        'problem',
        'proxy',
        'screen',
        'screenitem',
        'script',
        'service',
        'servicesla',
        'template',
        'templatescreen',
        'templatescreenitem',
        'trend',
        'trigger',
        'triggerprototype',
        'user',
        'usergroup',
        'usermacro',
        'usermedia',
        'valuemap',
        )


    method_bool = {}
    method_bool['application'] = ['inherited', 'templated']
    method_bool['graph'] = ['templated', 'inherited']
    method_bool['graphprototype'] = ['templated', 'inherited']
    method_bool['hostprototype'] = ['inherited']
    method_bool['httptest'] = ['inherited', 'monitored', 'templated']

    method_flag = {}
    method_flag['image'] = ['select_image']

    method_ids = {}
    method_ids['action'] = ['actionid', 'groupid', 'hostid', 'triggerid', 'mediatypeid', 'usrgrpid', 'userid', 'scriptid']
    method_ids['alert'] = ['alertid', 'actionid', 'eventid', 'groupid', 'hostid', 'mediatypeid', 'objectid', 'userid']
    method_ids['application'] = ['applicationid', 'groupid', 'hostid', 'itemid', 'templateid']
    method_ids['correlation'] = ['correlationid']
    method_ids['dcheck'] = ['dcheckid', 'druleid', 'dserviceid']
    method_ids['dhost'] = ['dhostid', 'druleid', 'dserviceid']
    method_ids['drule'] = ['dhostid', 'druleid', 'dserviceid']
    method_ids['dservice'] = ['dserviceid', 'dhostid', 'dcheckid', 'druleid']
    method_ids['event'] = ['eventid', 'groupid', 'hostid', 'objectid', 'applicationid']
    method_ids['graph'] = ['graphid', 'groupid', 'templateid', 'hostid', 'itemid']
    method_ids['graphitem'] = ['gitemid', 'graphid', 'itemid']
    method_ids['graphprototype'] = ['discoveryid', 'graphid', 'groupid', 'hostid', 'itemid', 'templateid']
    #method_ids['history'] = ['hostid', 'itemid']
    method_ids['host'] = ['groupid', 'applicationid', 'dserviceid', 'graphid', 'hostid', 'httptestid', 'interfaceid', 'itemid', 'maintenanceid', 'proxyid', 'templateid', 'triggerid']
    method_ids['hostgroup'] = ['graphid', 'groupid', 'hostid', 'maintenanceid', 'templateid', 'triggerid']
    method_ids['hostinterface'] = ['hostid', 'interfaceid', 'itemid', 'triggerid', 'nodeid']
    method_ids['hostprototype'] = ['hostid', 'discoveryid']
    method_ids['httptest'] = ['applicationid', 'groupid', 'hostid', 'httptestid', 'templateid']
    method_ids['iconmap'] = ['iconmapid', 'sysmapid']
    method_ids['image'] = ['imageid', 'sysmapid']
    method_ids['item'] = ['itemid', 'groupid', 'templateid', 'hostid', 'proxyid', 'interfaceid', 'graphid', 'triggerid', 'applicationid']
    method_ids['itemprototype'] = ['discoveryid', 'graphid', 'hostid', 'itemid', 'templateid', 'triggerid']
    method_ids['maintenance'] = ['groupid', 'hostid', 'maintenanceid']
    method_ids['map'] = ['sysmapid', 'userid']
    method_ids['mediatype'] = ['mediatypeid', 'mediaid', 'userid']
    method_ids['problem'] = ['eventid', 'groupid', 'hostid', 'objectid', 'applicationid']
    method_ids['proxy'] = ['proxyid']
    method_ids['screen'] = ['screenid', 'userid', 'screenitemid']
    method_ids['screenitem'] = ['screenitemid', 'screenid']
    method_ids['script'] = ['groupid', 'hostid', 'scriptid', 'usrgrpid']
    method_ids['service'] = ['serviceid', 'parentid', 'childid']
    method_ids['template'] = ['templateid', 'groupid', 'parentTemplateid', 'hostid', 'graphid', 'itemid', 'triggerid']
    method_ids['templatescreen'] = ['hostid', 'screenid', 'screenitemid', 'templateid']
    method_ids['templatescreenitem'] = ['screenid', 'screenitemid', 'hostid']
#    method_ids['trend'] = ['itemid']
    method_ids['trigger'] = ['triggerid', 'groupid', 'templateid', 'hostid', 'itemid', 'applicationid']
    method_ids['triggerprototype'] = ['applicationid', 'discoveryid', 'groupid', 'hostid', 'templateid', 'triggerid']
    method_ids['user'] = ['mediaid', 'mediatypeid', 'userid', 'usrgrpid']
    method_ids['usergroup'] = ['userid', 'usrgrpid']
    method_ids['usermacro'] = ['globalmacroid', 'groupid', 'hostid', 'hostmacroid', 'templateid']
#    method_ids['usermedia'] = ['mediaid', 'usrgrpid', 'userid', 'mediatypeid']
    method_ids['valuemap'] = ['valuemapid']

    method_sort = {}
    method_sort['action'] = ['actionid', 'name', 'status']
    method_sort['alert'] = ['alertid', 'clock', 'eventid', 'status']
    method_sort['application'] = ['applicationid', 'name']
    method_sort['correlation'] = ['correlationid', 'name', 'status']
    method_sort['dcheck'] = ['dcheckid', 'druleid']
    method_sort['dhost'] = ['dhostid', 'druleid']
    method_sort['drule'] = ['druleid', 'name']
    method_sort['dservice'] = ['dserviceid', 'dhostid', 'ip']
    method_sort['event'] = ['eventid', 'objectid', 'clock']
    method_sort['graph'] = ['graphid', 'name', 'graphtype']
    method_sort['graphitem'] = ['gitemid']
    method_sort['graphprototype'] = ['graphid', 'name', 'graphtype']
    #method_sort['history'] = ['itemid', 'clock']
    method_sort['host'] = ['hostid', 'host', 'name', 'status']
    method_sort['hostgroup'] = ['groupid', 'name']
    method_sort['hostinterface'] = ['interfaceid', 'dns', 'ip']
    method_sort['hostprototype'] = ['hostid', 'host', 'name', 'status']
    method_sort['httptest'] = ['httptestid', 'name']
    method_sort['iconmap'] = ['iconmapid', 'name']
    method_sort['image'] = ['imageid', 'name']
    method_sort['item'] = ['itemid', 'name', 'key_', 'delay', 'history', 'trends', 'type', 'status']
    method_sort['itemprototype'] = ['itemid', 'name', 'key_', 'delay', 'type', 'status']
    method_sort['maintenance'] = ['maintenanceid', 'name', 'maintenance_type']
    method_sort['map'] = ['name', 'width', 'height']
    method_sort['mediatype'] = ['mediatypeid']
    method_sort['problem'] = ['eventid']
    method_sort['proxy'] = ['hostid', 'host', 'status']
    method_sort['screen'] = ['screenid', 'name']
    method_sort['screenitem'] = ['screenitemid', 'screenid']
    method_sort['script'] = ['scriptid', 'name']
    method_sort['service'] = ['name', 'sortorder']
    method_sort['template'] = ['hostid', 'host', 'name']
    method_sort['templatescreen'] = ['screenid', 'name']
    method_sort['templatescreenitem'] = ['screenitemid', 'screenid']
    method_sort['trigger'] = ['triggerid', 'description', 'status', 'priority', 'lastchange', 'hostname']
    method_sort['triggerprototype'] = ['triggerid', 'description', 'status', 'priority']
    method_sort['user'] = ['userid', 'alias']
    method_sort['usergroup'] = ['usrgrpid', 'name']
    method_sort['usermacro'] = ['macro']
#    method_sort['usermedia'] = ['mediaid', 'userid', 'mediatypeid']
    method_sort['valuemap'] = ['valuemapid', 'name']

    method_time = {}
    method_time['alert'] = ['time_from', 'time_till']
    #method_time['history'] = ['time_from', 'time_till']

    runner = CliRunner()
    test_noargs(runner)

    for command in commands:
        test_command(runner, command)

    for command in commands:
        test_command_flag(runner, command, 'help')

        for flag in ['countOutput', 'editable', 'preservekeys', 'startSearch']:
            if command == 'autoregistration' or command == 'history':
                click.secho(command + ' does not support ' + flag, fg='red')
            else:
                test_command_comm(runner, command, flag)

        for flag in ['limit']:
            if command == 'autoregistration' or command == 'history':
                click.secho(command + ' does not support ' + flag, fg='red')
            else:
                test_command_comm_ints(runner, command, flag)

    for method in method_ids:
        for option in method_ids[method]:
            test_method_ids(runner, method, option)

    for method in method_bool:
        for option in method_bool[method]:
            test_method_bool(runner, method, option)

    for method in method_flag:
        for option in method_flag[method]:
            test_method_flag(runner, method, option)

    for method in method_sort:
        flag='sortfield'
        for value in method_sort[method]:
            test_method_sort(runner, method, flag, value)

    for method in method_time:
        for option in method_time[method]:
            test_method_times(runner, method, option)



if __name__ == '__main__':
    main()


