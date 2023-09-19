# Import standard libraries
from datetime import datetime

# Import installed libraries
import typer

# Import created libraries
from ..utils import wrapper
from ..constants import media as MediaConstants
from ..services import media as MediaService
from ..models import media as MediaModels
from ..services import extractor as ExtractorService
from ..models import extractor as ExtractorModels
from ..services import io as IOService


# Init Typer
app = typer.Typer()


@app.command()
@wrapper.typer_async
async def init(
    output_folder: str = typer.Option("./medias", "-o", "--output-folder"),
    game: bool = typer.Option(True),
    image: bool = typer.Option(True),
    book: bool = typer.Option(True),
    music: bool = typer.Option(True),
    video: bool = typer.Option(True)
):
    '''
    Create folders for your media storage
    '''
    await MediaService.init(
        output_folder,
        game,
        image,
        book,
        music,
        video
    )


@app.command()
@wrapper.typer_async
async def extract():
    '''
    Extract screenshots, clips, backdrops from extraction definition file
    '''
    data: ExtractorModels.ExtractorData = await ExtractorService.loadData(MediaConstants.EXTRACTOR_DEF_FILENAME)
    extractScript: str = await ExtractorService.getExtractScript(data)
    await IOService.writeFile('.', MediaConstants.EXTRACTOR_SCRIPT_FILENAME, extractScript)


@app.command()
@wrapper.typer_async
async def game(
    name: str,
    output_folder: str = typer.Option(".", "-o", "--output-folder"),
    image: bool = typer.Option(True),
    package: bool = typer.Option(True),
    patch: bool = typer.Option(True),
    mod: bool = typer.Option(True),
    wallpaper: bool = typer.Option(True),
    screenshot: bool = typer.Option(True),
    save: bool = typer.Option(True),
    todo: bool = typer.Option(True)
):
    '''
    Add folders to store a game
    '''
    await MediaService.game(
        name,
        output_folder,
        image,
        package,
        patch,
        mod,
        wallpaper,
        screenshot,
        save,
        todo
    )


@app.command()
@wrapper.typer_async
async def image(
    name: str,
    output_folder: str = typer.Option(".", "-o", "--output-folder"),
    type: MediaModels.ImageType = typer.Option("photo", "-t", "--type")
):
    '''
    Add folders to store some images
    '''
    await MediaService.image(
        name,
        output_folder,
        type
    )


@app.command()
@wrapper.typer_async
async def book(
    name: str,
    output_folder: str = typer.Option(".", "-o", "--output-folder"),
    type: MediaModels.BookType = typer.Option("book", "-t", "--type"),
    author_name: str = typer.Option(None, "-an", "--author-name")
):
    '''
    Add folders to store a book
    '''
    await MediaService.book(
        name,
        output_folder,
        type,
        author_name
    )


@app.command()
@wrapper.typer_async
async def music(
    name: str,
    output_folder: str = typer.Option(".", "-o", "--output-folder"),
    artist_name: str = typer.Option(None, "-an", "--artist-name")
):
    '''
    Add folders to store some musics
    '''
    await MediaService.music(
        name,
        output_folder,
        artist_name
    )


@app.command()
@wrapper.typer_async
async def serie(
    name: str,
    output_folder: str = typer.Option(".", "-o", "--output-folder"),
    type: MediaModels.SerieType = typer.Option("serie", "-t", "--type"),
    db_id_type: MediaModels.MediaDbIdType = typer.Option(
        "imdb", "-db", "--db-type"),
    db_id: str = typer.Option(None, "-id", "--db-id"),
    nb_season: int = typer.Option(0, "-ns", "--nb-season"),
    wallpaper: bool = typer.Option(True),
    screenshot: bool = typer.Option(True),
    backdrop: bool = typer.Option(True),
    ost: bool = typer.Option(True),
    clip: bool = typer.Option(True),
    extra: bool = typer.Option(True),
    todo: bool = typer.Option(True)
):
    '''
    Add folders to store a serie
    '''
    await MediaService.serie(
        name,
        output_folder,
        type,
        db_id_type,
        db_id,
        nb_season,
        wallpaper,
        screenshot,
        backdrop,
        ost,
        clip,
        extra,
        todo
    )


@app.command()
@wrapper.typer_async
async def movie(
    name: str,
    output_folder: str = typer.Option(".", "-o", "--output-folder"),
    year: int = typer.Option(datetime.now().year, "-y", "--year"),
    db_id_type: MediaModels.MediaDbIdType = typer.Option(
        "imdb", "-db", "--db-type"),
    db_id: str = typer.Option(None, "-id", "--db-id"),
    extrafanart: bool = typer.Option(True),
    screenshot: bool = typer.Option(True),
    clip: bool = typer.Option(True),
    todo: bool = typer.Option(True)
):
    '''
    Add folders to store a movie
    '''
    await MediaService.movie(
        name,
        output_folder,
        year,
        db_id_type,
        db_id,
        extrafanart,
        screenshot,
        clip,
        todo
    )
