import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve drules')
@options.add_options(options.dhostids)
@options.add_options(options.druleids)
@options.add_options(options.dserviceids)
@options.add_options(options.selectDChecks)
@options.add_options(options.selectDHosts)
@options.add_options(options.limitSelects)
@click.option('--sortfield', type=click.Choice(['druleid', 'name']))
@options.add_options(options.countOutput)
@options.add_options(options.editable)
@options.add_options(options.excludeSearch)
@options.add_options(options.filter)
@options.add_options(options.limit)
@options.add_options(options.nodeids)
@options.add_options(options.output)
@options.add_options(options.preservekeys)
@options.add_options(options.search)
@options.add_options(options.searchByAny)
@options.add_options(options.searchWildcardsEnabled)
@options.add_options(options.sortorder)
@options.add_options(options.startSearch)
@click.pass_obj
def drule(zart, sortfield, **kwargs):
    """This command retrieves drules."""
    zart.command = 'drule'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
