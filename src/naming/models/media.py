# Import standard libraries
from enum import Enum


class ImageType(str, Enum):
    screenshot = "screenshot"
    wallpaper = "wallpaper"
    photo = "photo"


class BookType(str, Enum):
    audiobook = "audiobook"
    book = "book"
    comic = "comic"
    manga = "manga"
    manhwa = "manhwa"
    manhua = "manhua"
    webtoon = "webtoon"


class SerieType(str, Enum):
    serie = "serie"
    anime = "anime"


class MediaDbIdType(str, Enum):
    imdb = "imdb"
    tvdb = "tvdb"
    tmdb = "tmdb"
