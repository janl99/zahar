import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve usermedias')
@common.add_options(common.mediaids)
@common.add_options(common.usrgrpids)
@common.add_options(common.userids)
@common.add_options(common.mediatypeids)
@click.option('--sortfield', type=click.Choice(['mediaid', 'userid', 'mediatypeid']))
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
def usermedia(zart, sortfield, **kwargs):
    """This command retrieves usermedias."""
    zart.command = 'usermedia'
    if sortfield:
        zart.sortfield = sortfield
    engine.engine(zart, **kwargs)
