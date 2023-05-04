# Import installed libraries
from json import dumps

# Import created libraries
from . import io as IOService


async def createTodoFile(filePath: str, datas: dict):
    '''
    Create todo file with data provided.
    '''
    print(f"Create todo file : {filePath}")
    todoJson: dict = {'media': False}
    if isinstance(datas, dict):
        for data in datas:
            todoJson[data] = False
    else:
        raise Exception("Bad data format !")
    await IOService.createFolder(filePath)
    await IOService.writeFile(filePath, "TODO.json", dumps(todoJson, indent=4))


async def getFormattedName(name: str) -> str:
    '''
    Format name from Serie's Name to series_name.
    '''
    formattedName: str = name.upper().lower()
    formattedName = formattedName.replace("'", "")
    formattedName = formattedName.replace(" ", "_")
    return formattedName
