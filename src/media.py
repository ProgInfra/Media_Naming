# Import standard libraries
from os import path
from datetime import datetime

# Import installed libraries
import typer

# Import created libraries
from . import utils
from . import models


# Init Typer
app = typer.Typer()


@app.command()
def init(
    output_folder: str = typer.Option(".", "-o", "--output-folder"),
    game: bool = typer.Option(True),
    image: bool = typer.Option(True),
    book: bool = typer.Option(True),
    music: bool = typer.Option(True),
    video: bool = typer.Option(True)
  ):
  '''
  Create folders for your media storage
  '''
  mediaFolders = {}

  if game: mediaFolders['games'] = None

  if image:
    mediaFolders['images'] = {
      'screenshots': None,
      'wallpapers': None,
      'photos': None,
    }

  if book:
    mediaFolders['books'] = {
      'audiobooks': None,
      'books': None,
      'comics': None,
      'mangas': None,
      'manhwas': None,
      'manhuas': None,
      'webtoons': None,
    }

  if music: mediaFolders['musics'] = None

  if video: mediaFolders['videos'] = {
    'movies': None,
    'series': None,
    'animes': None,
    'divers': None,
  }

  utils.createFolders(
    utils.getFormattedName(output_folder),
    mediaFolders
  )


@app.command()
def game(
    name: str,
    media_folder: str = typer.Option(".", "-m", "--media-folder"),
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
  gameFolders = {}
  gamePath = path.join(media_folder, f"games")

  gameName = utils.getFormattedName(name)
  gameFolders[gameName] = {}

  if image: gameFolders[gameName]['images'] = None
  if package: gameFolders[gameName]['packages'] = None
  if patch: gameFolders[gameName]['patches'] = None
  if mod: gameFolders[gameName]['mods'] = None
  if wallpaper: gameFolders[gameName]['wallpapers'] = None
  if screenshot: gameFolders[gameName]['screenshots'] = None
  if save: gameFolders[gameName]['saves'] = None
  if todo: utils.createTodoFile(f"{gamePath}/{gameName}", gameFolders[gameName])

  utils.createFolders(gamePath, gameFolders)


@app.command()
def image(
    name: str,
    media_folder: str = typer.Option(".", "-m", "--media-folder"),
    type: models.ImageType = typer.Option("photo", "-t", "--type")
  ):
  '''
  Add folders to store some images
  '''
  imageFolders = {}
  imagePath = path.join(media_folder, f"images/{type}s")

  imageFolders[utils.getFormattedName(name)] = None

  utils.createFolders(imagePath, imageFolders)


@app.command()
def book(
    name: str,
    media_folder: str = typer.Option(".", "-m", "--media-folder"),
    type: models.BookType = typer.Option("book", "-t", "--type"),
    author_name: str = typer.Option(None, "-an", "--author-name")
  ):
  '''
  Add folders to store a book
  '''
  bookFolders = {}
  bookPath = path.join(media_folder, f"books/{type}s")

  bookFolders[utils.getFormattedName(name)] = None

  if author_name:
    bookPath = path.join(bookPath, utils.getFormattedName(author_name))

  utils.createFolders(bookPath, bookFolders)


@app.command()
def music(
    name: str,
    media_folder: str = typer.Option(".", "-m", "--media-folder"),
    artist_name: str = typer.Option(None, "-an", "--artist-name")
  ):
  '''
  Add folders to store some musics
  '''
  musicFolders = {}
  musicPath = path.join(media_folder, f"musics")

  musicFolders[utils.getFormattedName(name)] = None

  if artist_name:
    musicPath = path.join(musicPath, utils.getFormattedName(artist_name))

  utils.createFolders(musicPath, musicFolders)


@app.command()
def serie(
    name: str,
    media_folder: str = typer.Option(".", "-m", "--media-folder"),
    type: models.SerieType = typer.Option("serie", "-t", "--type"),
    db_id_type: models.DbIdType = typer.Option("imdb", "-db", "--db-type"),
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
  serieFolders = {}
  seriePath = path.join(media_folder, f"videos/{type}s")

  serieName = f"{utils.getFormattedName(name)}"
  if db_id:
    serieName = f"{serieName}_[{db_id_type}id-{db_id}]"
  serieFolders[serieName] = {}

  serieBaseFolders = {}
  if wallpaper: serieBaseFolders["wallpapers"] = None
  if screenshot: serieBaseFolders["screenshots"] = None
  if backdrop: serieBaseFolders["backdrops"] = None
  if ost: serieBaseFolders["theme-music"] = None
  if clip: serieBaseFolders["clips"] = None
  if extra: serieBaseFolders["extras"] = None

  if nb_season > 0:
    for i in range(nb_season):
      seasonName = f"season_{i + 1:02d}"
      serieFolders[serieName][seasonName] = serieBaseFolders
      if todo: utils.createTodoFile(f"{seriePath}/{serieName}/{seasonName}", serieBaseFolders)

  utils.createFolders(seriePath, serieFolders)


@app.command()
def movie(
    name: str,
    media_folder: str = typer.Option(".", "-m", "--media-folder"),
    year: int = typer.Option(datetime.now().year, "-y", "--year"),
    db_id_type: models.DbIdType = typer.Option("imdb", "-db", "--db-type"),
    db_id: str = typer.Option(None, "-id", "--db-id"),
    extrafanart: bool = typer.Option(True),
    screenshot: bool = typer.Option(True),
    clip: bool = typer.Option(True),
    todo: bool = typer.Option(True)
  ):
  '''
  Add folders to store a movie
  '''
  movieFolders = {}
  moviePath = path.join(media_folder, f"videos/movies")

  movieName = f"{utils.getFormattedName(name)}_({year})"
  if db_id:
    movieName = f"{movieName}_[{db_id_type}id-{db_id}]"
  movieFolders[movieName] = {}

  if extrafanart: movieFolders[movieName]["extrafanart"] = None
  if screenshot: movieFolders[movieName]["screenshots"] = None
  if clip: movieFolders[movieName]["clips"] = None
  if todo: utils.createTodoFile(f"{moviePath}/{movieName}", movieFolders[movieName])

  utils.createFolders(moviePath, movieFolders)