class Screenshot:
    name: str = None
    file: str
    time: str


class Clip:
    name: str = None
    file: str
    start: str
    stop: str = None
    duration: str = None


class Backdrop:
    name: str = None
    file: str
    start: str
    stop: str = None
    duration: str = None


class ExtractorData:
    screenshots: list[Screenshot] = []
    clips: list[Clip] = []
    backdrops: list[Backdrop] = []
