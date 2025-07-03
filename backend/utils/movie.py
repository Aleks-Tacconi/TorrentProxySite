import os
from typing import TypedDict

import tmdbsimple as tmdb
from dotenv import load_dotenv
from torrent_sites.torrent_site import SearchResult

load_dotenv()

tmdb.API_KEY = os.getenv("MOVIES")


class Metadata(TypedDict):
    title: str
    year: str
    cover_url: str
    link: str
    id: str


class Movie:
    __search = tmdb.Search()

    def __init__(self, title: str) -> None:
        self.__title = title

    def metadata(self) -> Metadata | None:
        response = self.__search.movie(query=self.__title)["results"]

        if not response:
            response = self.__search.movie(query=self.__title[:len(self.__title) - 5])["results"]

        if not response:
            return None

        title_lower = self.__title.lower().strip()
        movie = next((m for m in response if m["title"].lower() == title_lower), response[0])

        poster_path = movie["poster_path"]

        if poster_path is None:
            path = "https://placehold.co/250x350?text=%3F&format=png"
        else:
            path = f"https://image.tmdb.org/t/p/w500{poster_path}"

        return Metadata(
            title=str(movie["title"]),
            year=str(movie["release_date"][:4]),
            cover_url=path,
            link="",
            id="",
        )


def movie_metadata(result: SearchResult) -> Metadata | None:
    metadata = Movie(result["title"]).metadata()

    if metadata is not None:
        metadata["link"] = result["torrent_access_point"]
        metadata["id"] = result["id"]

    return metadata

def local_movie(title: str, path: str) -> Metadata | None:
    metadata = Movie(title).metadata()

    if metadata is not None:
        metadata["link"] = path
        metadata["id"] = "local"

    return metadata
