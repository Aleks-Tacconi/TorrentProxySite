import bencodepy
import requests


def torrent_name(url) -> str:
    response = requests.get(url, timeout=100)
    torrent_dict = bencodepy.decode(response.content)
    return torrent_dict[b"info"][b"name"].decode("utf-8")
