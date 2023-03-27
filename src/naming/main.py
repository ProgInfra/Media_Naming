# Import installed libraries
import typer

# Import created libraries
from .commands import media
from .services import utils
from .utils import wrapper


# Init Typer
app = typer.Typer()


@app.command()
@wrapper.typer_async
async def init(
    output_folder: str = typer.Option(".", "-o", "--output-folder"),
    admin: bool = typer.Option(True),
    project: bool = typer.Option(True),
    server: bool = typer.Option(True),
    sys: bool = typer.Option(True),
    linux: bool = typer.Option(True),
    windows: bool = typer.Option(True)
  ):
  '''
  Create basics folders for your main operating system
  '''
  systemFolders = {
    'documents': None,
  }

  if admin:
    systemFolders['admin'] = {
      'accounts': None,
      'backups': None,
      'documents': None,
    }

  if project: systemFolders['projects'] = None
  if server: systemFolders['servers'] = None

  if sys:
    systemFolders['sys'] = {
      'backups': None,
      'downloads': None,
      'gnos': None,
      'tmp': None,
      'vm': None,
    }

    if linux and windows:
      systemFolders['sys']['games'] = {'linux': None, 'windows': None}
      systemFolders['sys']['softwares'] = {'linux': None, 'windows': None}
    else:
      systemFolders['sys']['games'] = None
      systemFolders['sys']['softwares'] = None

  await utils.createFolders(
    await utils.getFormattedName(output_folder),
    systemFolders
  )


app.add_typer(media.app, name="media")


if __name__ == "__main__":
  app()
