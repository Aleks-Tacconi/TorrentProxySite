from typing import List

import internetarchive

from .torrent_site import SearchResult, TorrentInfo, TorrentSite


class FeatureFilms(TorrentSite):
    def __init__(self) -> None:
        super().__init__("archive")

    def search(self, query: str) -> List[SearchResult]:
        q = f"collection:feature_films AND mediatype:movies AND title:({query})"
        results = []
        search = internetarchive.search_items(q, fields=["identifier", "title"])

        for i, item in enumerate(search):
            if i >= 50:
                break

            identifier = item.get("identifier")
            title = item.get("title", identifier)
            results.append(
                SearchResult(
                    title=title,
                    torrent_access_point=f"https://archive.org/details/{identifier}",
                    id=self.key,
                )
            )

        return results

    def get_torrents(self, torrent_access_point: str) -> List[TorrentInfo]:
        identifier = torrent_access_point.rstrip("/").split("/")[-1]
        item = internetarchive.get_item(identifier)

        torrents = []
        for f in item.get_files():
            if f.name.endswith(".torrent"):
                torrents.append(TorrentInfo(name=f.name, url=f.url))

        return torrents
