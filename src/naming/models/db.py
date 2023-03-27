# Import standard libraries
from enum import Enum


class DbIdType(str, Enum):
  imdb = "imdb"
  tvdb = "tvdb"
  tmdb = "tmdb"
