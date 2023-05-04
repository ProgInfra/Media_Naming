# Import created libraries
from ..constants import os as OS_CONSTANTS
from . import io as IOService
from . import utils as UtilsService


async def init(
    outputFolder: str,
    admin: bool,
    project: bool,
    server: bool,
    sys: bool,
    linux: bool,
    windows: bool
):
    osFolderTree = await getOSFolderTree(
        admin,
        project,
        server,
        sys,
        linux,
        windows
    )
    formattedOutputFolder = await UtilsService.getFormattedName(outputFolder)
    await IOService.createFolders(
        formattedOutputFolder,
        osFolderTree
    )


async def getOSFolderTree(
    admin: bool,
    project: bool,
    server: bool,
    sys: bool,
    linux: bool,
    windows: bool
):
    os = OS_CONSTANTS.OS_BASE
    if admin:
        os = os | OS_CONSTANTS.OS_ADMIN
    if project:
        os = os | OS_CONSTANTS.OS_PROJECT
    if server:
        os = os | OS_CONSTANTS.OS_SERVER
    if sys:
        os = os | OS_CONSTANTS.OS_SYS_BASE
    if linux and windows:
        os = os | OS_CONSTANTS.OS_SYS_LINUX_WINDOWS
    else:
        os = os | OS_CONSTANTS.OS_SYS_BASIC
    return os
