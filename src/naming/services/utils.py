# Import installed libraries
from os import path, makedirs
from json import dumps


async def createFolder(folderPath: str):
    '''
    Create folder from path.
    '''
    print(f"Create folder : {folderPath}")
    try:
        makedirs(folderPath, exist_ok=True)
    except OSError as error:
        print(f"Error when create folder : {folderPath}")
        raise error
    print("Create complete !")


async def createFolders(basePath: str, folders: dict, subfolder: bool = False) -> int:
    '''
    Create folders from base path and folders tree.
    '''
    print(f"Create folders in base path : {basePath}")
    folderCounter = 0
    if isinstance(folders, dict):
        for folder in folders:
            folderPath: str = path.join(basePath, folder)
            await createFolder(folderPath)
            folderCounter += 1
            if folders[folder] is not None and isinstance(folders[folder], dict):
                folderCounter += await createFolders(folderPath, folders[folder], True)
    else:
        raise Exception("Bad folders tree format !")
    if not subfolder:
        print(f"Create complete ! ({folderCounter} folders created)")
    return folderCounter


async def writeFile(filePath: str, fileName: str, data: str):
    '''
    Write file with data provided
    '''
    try:
        with open(f"{filePath}/{fileName}", "w") as file:
            await file.write(data)
    except IOError as error:
        print(f"Error when write file : {filePath}/{fileName}")
        raise error


async def createTodoFile(filePath: str, datas: dict):
    '''
    Create todo file with data provided.
    '''
    print(f"Create todo file : {filePath}")
    todoJson: dict = {}
    if isinstance(datas, dict):
        for data in datas:
            todoJson[data] = False
    else:
        raise Exception("Bad data format !")
    await writeFile(filePath, "TODO.json", dumps(todoJson))


async def getFormattedName(name: str) -> str:
    '''
    Format name from Serie's Name to series_name.
    '''
    formattedName: str = name.upper().lower()
    formattedName = formattedName.replace("'", "")
    formattedName = formattedName.replace(" ", "_")
    return formattedName
