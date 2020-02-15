import logging
import click
from commands import options
import engine


@click.command(short_help='retrieve itemprototypes')
@options.add_options(options.discoveryids)
@options.add_options(options.graphids)
@options.add_options(options.hostids)
@options.add_options(options.inherited)
@options.add_options(options.itemids)
@options.add_options(options.monitored)
@options.add_options(options.templated)
@options.add_options(options.templateids)
@options.add_options(options.triggerids)
@options.add_options(options.selectApplications)
@options.add_options(options.selectApplicationPrototypes)
@options.add_options(options.selectDiscoveryRule)
@options.add_options(options.selectGraphs)
@options.add_options(options.selectHosts)
@options.add_options(options.selectTriggers)
@options.add_options(options.selectPreprocessing)
@options.add_options(options.filter)
@options.add_options(options.limitSelects)
@click.option('--sortfield', type=click.Choice(['itemid', 'name', 'key_', 'delay', 'type', 'status']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.limit)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.search)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
@click.pass_obj
def itemprototype(zart, sortfield, **kwargs):
    """This command retrieves itemprototypes."""
    zart.command = 'itemprototype'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
