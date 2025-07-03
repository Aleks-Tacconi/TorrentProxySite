import threading
from typing import List

from rapidfuzz import fuzz
from utils import WebScraper, torrent_name

from .torrent_site import SearchResult, TorrentInfo, TorrentSite


class PublicDomainTorrents(TorrentSite):
    def __init__(self) -> None:
        super().__init__("pdt")

        self.__movies = []

        threading.Thread(target=self.__load_movies).start()

    def __load_movies(self) -> None:
        url = "https://www.publicdomaintorrents.info/nshowcat.html?category=ALL"
        prefix = "https://www.publicdomaintorrents.info/nshowmovie.html?movieid"
        web_scraper = WebScraper(url)

        for link in web_scraper.find_all():
            if link.startswith(prefix):
                scraper = WebScraper(link)
                title = scraper.find_first_tag("h3")

                self.__movies.append(
                    SearchResult(title=title, torrent_access_point=link, id=self.key)
                )

    def search(self, query: str) -> List[SearchResult]:
        threshold = 60
        results = []
        for movie in self.__movies:
            score = fuzz.partial_ratio(query.lower(), movie["title"].lower())
            if score >= threshold:
                results.append((score, movie))

        return [item for _, item in sorted(results, reverse=True, key=lambda x: x[0])]

    def get_torrents(self, torrent_access_point: str) -> List[TorrentInfo]:
        web_scraper = WebScraper(torrent_access_point)
        links = set(
            link for link in web_scraper.find_all() if link.endswith(".torrent")
        )

        torrents_lst = []
        for link in links:
            name = torrent_name(link)
            torrents_lst.append(TorrentInfo(name=name, url=link))

        return torrents_lst
