# Import installed libraries
import typer

# Import created libraries
from ..cli import media
from ..utils import wrapper
from ..services import os as OSService


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
    await OSService.init(
        output_folder,
        admin,
        project,
        server,
        sys,
        linux,
        windows
    )


app.add_typer(media.app, name="media")
