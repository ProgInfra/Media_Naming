# Import created libraries
from ..constants import media as MEDIA_CONSTANTS
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


async def isMediaFolder():
    '''
    Detect if there are a media folder to create folder into.
    '''
    pass


async def game():
    pass


async def image():
    pass


async def book():
    pass


async def music():
    pass


async def serie():
    pass


async def movie():
    pass
