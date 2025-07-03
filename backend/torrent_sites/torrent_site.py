from abc import ABCMeta, abstractmethod
from typing import List, TypedDict


class TorrentInfo(TypedDict):
    name: str
    url: str


class SearchResult(TypedDict):
    title: str
    torrent_access_point: str
    id: str


class TorrentSite(metaclass=ABCMeta):
    def __init__(self, key: str) -> None:
        self.key = key

    @abstractmethod
    def search(self, query: str) -> List[SearchResult]: ...

    @abstractmethod
    def get_torrents(self, torrent_access_point: str) -> List[TorrentInfo]: ...
