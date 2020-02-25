import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve hosts')
@options.add_options(options.groupids)
@options.add_options(options.applicationids)
@options.add_options(options.dserviceids)
@options.add_options(options.graphids)
@options.add_options(options.hostids)
@options.add_options(options.httptestids)
@options.add_options(options.interfaceids)
@options.add_options(options.itemids)
@options.add_options(options.maintenanceids)
@options.add_options(options.monitored_hosts)
@options.add_options(options.proxy_hosts)
@options.add_options(options.proxyids)
@options.add_options(options.templated_hosts)
@options.add_options(options.templateids)
@options.add_options(options.triggerids)
@options.add_options(options.with_items)
@options.add_options(options.with_item_prototypes)
@options.add_options(options.with_simple_graph_item_prototypes)
@options.add_options(options.with_applications)
@options.add_options(options.with_graphs)
@options.add_options(options.with_historical_items)
@options.add_options(options.with_graph_prototypes)
@options.add_options(options.with_httptests)
@options.add_options(options.with_monitored_httptests)
@options.add_options(options.with_monitored_items)
@options.add_options(options.with_monitored_triggers)
@options.add_options(options.with_simple_graph_items)
@options.add_options(options.with_triggers)
@options.add_options(options.withProblemsSuppressed)
@options.add_options(options.withInventory)
@options.add_options(options.evaltype)
@options.add_options(options.severities)
@options.add_options(options.tags)
@options.add_options(options.inheritedTags)
@options.add_options(options.selectApplications)
@options.add_options(options.selectDiscoveries)
@options.add_options(options.selectDiscoveryRule)
@options.add_options(options.selectGraphs)
@options.add_options(options.selectGroups)
@options.add_options(options.selectHostDiscovery)
@options.add_options(options.selectHttpTests)
@options.add_options(options.selectInterfaces)
@options.add_options(options.selectInventory)
@options.add_options(options.selectItems)
@options.add_options(options.selectMacros)
@options.add_options(options.selectParentTemplates)
@options.add_options(options.selectScreens)
@options.add_options(options.selectTags)
@options.add_options(options.selectInheritedTags)
@options.add_options(options.selectTriggers)
@options.add_options(options.filter)
@options.add_options(options.limitSelects)
@options.add_options(options.search)
@options.add_options(options.searchInventory)
@click.option('--sortfield', type=click.Choice(['hostid', 'host', 'name', 'status']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.limit)
@options.add_options(options.nodeids)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
@click.pass_obj
def host(zart, sortfield, **kwargs):
    """This command retrieves hosts."""
    zart.command = 'host'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
