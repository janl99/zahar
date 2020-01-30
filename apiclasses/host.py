import click

from apiclasses import common
from apiclasses import outputformat


@click.command(short_help='retrieve hosts')
@common.add_options(common.groupids)
@common.add_options(common.applicationids)
@common.add_options(common.dserviceids)
@common.add_options(common.graphids)
@common.add_options(common.hostids)
@common.add_options(common.httptestids)
@common.add_options(common.interfaceids)
@common.add_options(common.itemids)
@common.add_options(common.maintenanceids)
@common.add_options(common.monitored_hosts)
@common.add_options(common.proxy_hosts)
@common.add_options(common.proxyids)
@common.add_options(common.templated_hosts)
@common.add_options(common.templateids)
@common.add_options(common.triggerids)
@common.add_options(common.with_items)
@common.add_options(common.with_applications)
@common.add_options(common.with_graphs)
@common.add_options(common.with_httptests)
@common.add_options(common.with_monitored_httptests)
@common.add_options(common.with_monitored_items)
@common.add_options(common.with_monitored_triggers)
@common.add_options(common.with_simple_graph_items)
@common.add_options(common.with_triggers)
@common.add_options(common.withInventory)
# todo: for future use once we sort out passing queries
#@common.add_options(common.selectGroups)
#@common.add_options(common.selectApplications)
#@common.add_options(common.selectDiscoveries)
#@common.add_options(common.selectDiscoveryRule)
#@common.add_options(common.selectGraphs)
#@common.add_options(common.selectHostDiscovery)
#@common.add_options(common.selectHttpTests)
#@common.add_options(common.selectInterfaces)
#@common.add_options(common.selectInventory)
#@common.add_options(common.selectItems)
#@common.add_options(common.selectMacros)
#@common.add_options(common.selectParentTemplates)
#@common.add_options(common.selectScreens)
#@common.add_options(common.selectTriggers)
@common.add_options(common.filter)
@common.add_options(common.limitSelects)
@common.add_options(common.search)
@common.add_options(common.searchInventory)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['hostid', 'host', 'name', 'status']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.excludeSearch)
@common.add_options(common.limit)
@common.add_options(common.output)
@common.add_options(common.preservekeys)
@common.add_options(common.searchByAny)
@common.add_options(common.searchWildcardsEnabled)
@common.add_options(common.sortorder)
@common.add_options(common.startSearch)
@common.add_options(common.outputformat)
@click.pass_obj
def host(zart, sortfield, **kwargs):
    """This command retrieves hosts."""

    #ben magic, throw away False and Empty items
    keywords = {k:v for k,v in kwargs.items() if v}

    # setting the default in common passes a tuple
    if kwargs.get('output') and 'extend' in kwargs.get('output'):
        keywords['output'] = 'extend'

    # todo: sortfield needs to move to common
    keywords['sortfield'] = sortfield if sortfield else None

    try:
        obj = zart.zapi.host.get(**keywords)
    except:
        # todo: fix bare except above and write a better error messages
        click.secho('Error: todo.',
                    fg='red', err=True)

    if 'countOutput' in keywords and keywords['countOutput']:
        click.echo(obj)
    else:
        outputformat.outputformat(obj, keywords['outputformat'])

    if 'limit' in keywords and len(obj) >= keywords['limit']:
        click.secho('Warning: row limit matches records returned,'
                    ' there may be data you are not seeing.',
                    fg='yellow', err=True)
