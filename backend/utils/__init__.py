from .downloader import download, torrent
from .local import find_movies
from .movie import Movie, movie_metadata
from .torrent_utils import torrent_name
from .web_scraper import WebScraper

__all__ = [
    "WebScraper",
    "torrent_name",
    "Movie",
    "movie_metadata",
    "download",
    "torrent",
    "find_movies",
]
