import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve scripts')
@common.add_options(common.groupids)
@common.add_options(common.hostids)
@common.add_options(common.scriptids)
@common.add_options(common.usrgrpids)
@common.add_options(common.selectGroups)
@common.add_options(common.selectHosts)
@click.option('--sortfield', type=click.Choice(['scriptid', 'name']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.excludeSearch)
@common.add_options(common.filter)
@common.add_options(common.limit)
@common.add_options(common.output)
@common.add_options(common.preservekeys)
@common.add_options(common.search)
@common.add_options(common.searchByAny)
@common.add_options(common.searchWildcardsEnabled)
@common.add_options(common.sortorder)
@common.add_options(common.startSearch)
@common.add_options(common.outputformat)
@click.pass_obj
def script(zart, sortfield, **kwargs):
    """This command retrieves scripts."""
    zart.command = 'script'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
