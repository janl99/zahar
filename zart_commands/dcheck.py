import logging
import click
from zart_commands import options
import engine


@click.command(short_help='retrieve dchecks')
@options.add_options(options.dcheckids)
@options.add_options(options.druleids)
@options.add_options(options.dserviceids)
@click.option('--sortfield', type=click.Choice(['dcheckid', 'druleid']))
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
def dcheck(zart, sortfield, **kwargs):
    """This command retrieves dchecks."""
    zart.command = 'dcheck'
    logging.debug('zart.command: %s', zart.command)
    if sortfield:
        kwargs['sortfield'] = sortfield
        logging.debug('kwargs[\'sortfield\']: %s', kwargs['sortfield'])
    logging.debug(kwargs)
    engine.engine(zart, **kwargs)
