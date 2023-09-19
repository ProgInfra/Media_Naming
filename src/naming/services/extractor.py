# Import standard libraries
from pathlib import Path

# Import installed libraries
import json
import ffmpy

# Import created libraries
from ..models import extractor as ExtractorModels


async def loadData(
    fileName: str,
) -> ExtractorModels.ExtractorData:
    with open(fileName, 'r') as fileRaw:
        fileExt = Path(fileName).suffix
        if (fileExt == ".json"):
            return json.load(fileRaw)
        else:
            raise Exception(f"Bad format for file : {fileName}, ext = {fileExt}, available format are : json,yaml,yml")


async def getExtractScript(
    data: ExtractorModels.ExtractorData
) -> str:
    extractScript: str = "#!/bin/bash\n\n"

    # Extract Screenshots
    extractScript += "# Screenshots\n"
    for screenshot in data['screenshots']:
        print(f"Extract screenshot from {screenshot['file']} at {screenshot['time']}")
        extractScript += f'{await getScreenshotExtractScript(screenshot)}\n'
    extractScript += "\n"

    # Extract Clips
    extractScript += "# Clips\n"
    for clip in data['clips']:
        if "stop" in clip:
            print(f"Extract clip from {clip['file']} start from {clip['start']} and end to {clip['stop']}")
        if "duration" in clip:
            print(
                f"Extract clip from {clip['file']} start from {clip['start']} with a duration of {clip['duration']} s")
        extractScript += f'{await getClipExtractScript(clip)}\n'
    extractScript += "\n"

    # Extract Backdrops
    extractScript += "# Backdrops\n"
    for backdrop in data['backdrops']:
        if "stop" in backdrop:
            print(
                f"Extract backdrop from {backdrop['file']} start from {backdrop['start']} and end to {backdrop['stop']}")
        if "duration" in backdrop:
            print(
                f"Extract backdrop from {backdrop['file']} start from {backdrop['start']} with a duration of {backdrop['duration']} s")
        extractScript += f'{await getBackdropExtractScript(backdrop)}\n'
    extractScript += "\n"

    return extractScript


async def getScreenshotExtractScript(screenshot: ExtractorModels.Screenshot) -> str:
    videoFileName = Path(screenshot['file'])

    if 'name' in screenshot:
        fileName = f"screenshots/{videoFileName.stem}_screenshot_{screenshot['time'].replace(':', '-')}_{screenshot['name'].replace(' ', '-')}.png"
    else:
        fileName = f"screenshots/{videoFileName.stem}_screenshot_{screenshot['time'].replace(':', '-')}.png"

    inputs = {}
    outputs = {}

    inputs[screenshot['file']] = f'-ss "{screenshot["time"]}"'
    outputs[fileName] = '-frames:v 1'

    return ffmpy.FFmpeg(
        inputs=inputs,
        outputs=outputs
    ).cmd


async def getClipExtractScript(clip: ExtractorModels.Clip) -> str:
    videoFileName = Path(clip['file'])

    fileName = f"clips/{videoFileName.stem}_clip_from_{clip['start'].replace(':', '-')}"

    if 'stop' in clip:
        fileName += f"_to_{clip['stop'].replace(':', '-')}"
    elif 'duration' in clip:
        fileName += f"_during_{clip['duration'].replace(':', '-')}"
    else:
        print("stop and duration don't have to be present at the same time !")
        exit(1)

    if 'name' in clip:
        fileName += f"_{clip['name'].replace(' ', '-')}{videoFileName.suffix}"
    else:
        fileName += f"{videoFileName.suffix}"

    inputs = {}
    outputs = {}

    if 'stop' in clip:
        inputs[clip['file']] = f'-copyts -ss "{clip["start"]}"'
        outputs[fileName] = f'-t "{clip["stop"]}" -map 0 -c copy'
    if 'duration' in clip:
        inputs[clip['file']] = f'-ss "{clip["start"]}"'
        outputs[fileName] = f'-t "{clip["duration"]}" -map 0 -c copy'

    return ffmpy.FFmpeg(
        inputs=inputs,
        outputs=outputs
    ).cmd


async def getBackdropExtractScript(backdrop: ExtractorModels.Backdrop) -> str:
    videoFileName = Path(backdrop['file'])

    fileName = f"backdrops/{videoFileName.stem}_backdrop_from_{backdrop['start'].replace(':', '-')}"

    if 'stop' in backdrop:
        fileName += f"_to_{backdrop['stop'].replace(':', '-')}"
    elif 'duration' in backdrop:
        fileName += f"_during_{backdrop['duration'].replace(':', '-')}"
    else:
        print("stop and duration don't have to be present at the same time !")
        exit(1)

    if 'name' in backdrop:
        fileName += f"_{backdrop['name'].replace(' ', '-')}{videoFileName.suffix}"
    else:
        fileName += f"{videoFileName.suffix}"

    inputs = {}
    outputs = {}

    if 'stop' in backdrop:
        inputs[backdrop['file']] = f'-copyts -ss "{backdrop["start"]}"'
        outputs[fileName] = f'-t "{backdrop["stop"]}" -map 0 -c copy'
    if 'duration' in backdrop:
        inputs[backdrop['file']] = f'-ss "{backdrop["start"]}"'
        outputs[fileName] = f'-t "{backdrop["duration"]}" -map 0 -c copy'

    return ffmpy.FFmpeg(
        inputs=inputs,
        outputs=outputs
    ).cmd
