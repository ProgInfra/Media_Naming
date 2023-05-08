# Import standard libraries
from os import path

# Import created libraries
from ..constants import media as MEDIA_CONSTANTS
from ..models import media as MediaModels
from . import io as IOService
from . import utils as UtilsService


async def init(
    outputFolder: str,
    game: bool,
    image: bool,
    book: bool,
    music: bool,
    video: bool
):
    mediaFolderTree = await getMediaFolderTree(
        game,
        image,
        book,
        music,
        video
    )
    formattedOutputFolder = await UtilsService.getFormattedName(outputFolder)
    await IOService.createFolders(
        formattedOutputFolder,
        mediaFolderTree
    )


async def getMediaFolderTree(
    game: bool,
    image: bool,
    book: bool,
    music: bool,
    video: bool
):
    media = {}
    if game:
        media = media | MEDIA_CONSTANTS.MEDIA_GAME
    if image:
        media = media | MEDIA_CONSTANTS.MEDIA_IMAGE
    if book:
        media = media | MEDIA_CONSTANTS.MEDIA_BOOK
    if music:
        media = media | MEDIA_CONSTANTS.MEDIA_MUSIC
    if video:
        media = media | MEDIA_CONSTANTS.MEDIA_VIDEO
    return media


async def isMediaFolder(outputPath: str):
    '''
    Detect if there are a media folder to create folder into.
    '''
    folders = await IOService.listFolder(outputPath)
    if "medias" in folders:
        print("Medias Folder detected !")
        return True
    else:
        print("Medias Folder not detected, use of current folder instead !")
        return False


async def game(
    name: str,
    outputFolder: str,
    image: bool,
    package: bool,
    patch: bool,
    mod: bool,
    wallpaper: bool,
    screenshot: bool,
    save: bool,
    todo: bool
):
    if (await isMediaFolder(outputFolder)):
        gamePath = f"{outputFolder}/medias/games"
    else:
        gamePath = outputFolder

    gameFormattedName = await UtilsService.getFormattedName(name)
    gameFolders = {}
    gameFolders[gameFormattedName] = {}

    if image:
        gameFolders[gameFormattedName]['images'] = None
    if package:
        gameFolders[gameFormattedName]['packages'] = None
    if patch:
        gameFolders[gameFormattedName]['patches'] = None
    if mod:
        gameFolders[gameFormattedName]['mods'] = None
    if wallpaper:
        gameFolders[gameFormattedName]['wallpapers'] = None
    if screenshot:
        gameFolders[gameFormattedName]['screenshots'] = None
    if save:
        gameFolders[gameFormattedName]['saves'] = None
    if todo:
        await UtilsService.createTodoFile(f"{gamePath}/{gameFormattedName}", gameFolders[gameFormattedName])

    await IOService.createFolders(gamePath, gameFolders)


async def image(
    name: str,
    outputFolder: str,
    type: MediaModels.ImageType
):
    if (await isMediaFolder(outputFolder)):
        imagePath = f"{outputFolder}/medias/images/{type}s"
    else:
        imagePath = outputFolder

    imageFormattedName = await UtilsService.getFormattedName(name)
    imageFolders = {}
    imageFolders[imageFormattedName] = None

    await IOService.createFolders(imagePath, imageFolders)


async def book(
    name: str,
    outputFolder: str,
    type: MediaModels.BookType,
    authorName: str
):
    if (await isMediaFolder(outputFolder)):
        bookPath = f"{outputFolder}/medias/books/{type}s"
    else:
        bookPath = outputFolder

    bookFormattedName = await UtilsService.getFormattedName(name)
    bookFolders = {}
    bookFolders[bookFormattedName] = None

    if authorName:
        bookPath = path.join(bookPath, await UtilsService.getFormattedName(authorName))

    await IOService.createFolders(bookPath, bookFolders)


async def music(
    name: str,
    outputFolder: str,
    artistName: str
):
    if (await isMediaFolder(outputFolder)):
        musicPath = f"{outputFolder}/medias/musics"
    else:
        musicPath = outputFolder

    musicFormattedName = await UtilsService.getFormattedName(name)
    musicFolders = {}
    musicFolders[musicFormattedName] = None

    if artistName:
        musicPath = path.join(musicPath, await UtilsService.getFormattedName(artistName))

    await IOService.createFolders(musicPath, musicFolders)


async def serie(
    name: str,
    outputFolder: str,
    type: MediaModels.SerieType,
    dbIdType: MediaModels.MediaDbIdType,
    dbId: str,
    nbSeason: int,
    wallpaper: bool,
    screenshot: bool,
    backdrop: bool,
    ost: bool,
    clip: bool,
    extra: bool,
    todo: bool
):
    if (await isMediaFolder(outputFolder)):
        seriePath = f"{outputFolder}/medias/videos/{type}s"
    else:
        seriePath = outputFolder

    serieFormattedName = await UtilsService.getFormattedName(name)
    serieFolders = {}

    if dbId:
        serieFormattedName = f"{serieFormattedName}_[{dbIdType}id-{dbId}]"

    serieFolders[serieFormattedName] = {}

    serieBaseFolders = {}
    if wallpaper:
        serieBaseFolders["wallpapers"] = None
    if screenshot:
        serieBaseFolders["screenshots"] = None
    if backdrop:
        serieBaseFolders["backdrops"] = None
    if ost:
        serieBaseFolders["theme-music"] = None
    if clip:
        serieBaseFolders["clips"] = None
    if extra:
        serieBaseFolders["extras"] = None

    if nbSeason > 0:
        for i in range(nbSeason):
            seasonName = f"season_{i + 1:02d}"
            serieFolders[serieFormattedName][seasonName] = serieBaseFolders
            if todo:
                await UtilsService.createTodoFile(f"{seriePath}/{serieFormattedName}/{seasonName}", serieBaseFolders)
    else:
        serieFolders[serieFormattedName] = serieBaseFolders
        if todo:
            await UtilsService.createTodoFile(f"{seriePath}/{serieFormattedName}", serieBaseFolders)

    await IOService.createFolders(seriePath, serieFolders)


async def movie(
    name: str,
    outputFolder: str,
    year: int,
    dbIdType: MediaModels.MediaDbIdType,
    dbId: str,
    extrafanart: bool,
    screenshot: bool,
    clip: bool,
    todo: bool
):
    if (await isMediaFolder(outputFolder)):
        moviePath = f"{outputFolder}/medias/videos/movies"
    else:
        moviePath = outputFolder

    movieFormattedName = await UtilsService.getFormattedName(name)
    movieFormattedName = f"{movieFormattedName}_({year})"
    movieFolders = {}

    if dbId:
        movieFormattedName = f"{movieFormattedName}_[{dbIdType}id-{dbId}]"

    movieFolders[movieFormattedName] = {}

    if extrafanart:
        movieFolders[movieFormattedName]["extrafanart"] = None
    if screenshot:
        movieFolders[movieFormattedName]["screenshots"] = None
    if clip:
        movieFolders[movieFormattedName]["clips"] = None
    if todo:
        await UtilsService.createTodoFile(f"{moviePath}/{movieFormattedName}", movieFolders[movieFormattedName])

    await IOService.createFolders(moviePath, movieFolders)
