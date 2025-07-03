from typing import List

from .public_domain_torrents import PublicDomainTorrents
from .torrent_site import SearchResult, TorrentInfo
from .feature_films import FeatureFilms


class TorrentStore:
    def __init__(self) -> None:
        t2 = PublicDomainTorrents()
        t3 = FeatureFilms()

        self.__torrent_sites = {
            t2.key: t2,
            t3.key: t3,
        }

    def search(self, query: str) -> List[SearchResult]:
        results = []

        for site in self.__torrent_sites.values():
            results.extend(site.search(query))

        return results

    def get_torrents(self, key: str, torrent_access_point: str) -> List[TorrentInfo]:
        return self.__torrent_sites[key].get_torrents(torrent_access_point)
