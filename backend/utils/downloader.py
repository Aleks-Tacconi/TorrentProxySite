import os
import subprocess
import uuid

import requests

if not os.path.exists("./client/public/Data"):
    os.mkdir("./client/public/Data")

if not os.path.exists("./client/public/Data/torrents"):
    os.mkdir("./client/public/Data/torrents")

if not os.path.exists("./client/public/Data/movies"):
    os.mkdir("./client/public/Data/movies")

if not os.path.exists("./client/public/Data/downloading"):
    os.mkdir("./client/public/Data/downloading")


def download(url: str) -> str:
    random_name = f"{uuid.uuid4().hex}.torrent"
    save_path = os.path.join("client", "public", "Data", "torrents", random_name)

    response = requests.get(url, stream=True, timeout=100)
    response.raise_for_status()

    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    return save_path


def torrent(file_path: str) -> None:
    subprocess.run(
        ["webtorrent", file_path, "--out", "./client/public/Data/downloading"],
        check=True,
    )
