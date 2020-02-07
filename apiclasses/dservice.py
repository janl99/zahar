import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve dservices')
@common.add_options(common.dserviceids)
@common.add_options(common.dhostids)
@common.add_options(common.dcheckids)
@common.add_options(common.druleids)
@common.add_options(common.selectDRules)
@common.add_options(common.selectDHosts)
@common.add_options(common.selectHosts)
@common.add_options(common.limitSelects)
@click.option('--sortfield', type=click.Choice(['dserviceid', 'dhostid', 'ip']))
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
def dservice(zart, sortfield, **kwargs):
    """This command retrieves dservices."""
    zart.command = 'dservice'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
