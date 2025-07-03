import json
import os
from typing import List

from babelfish import Language
from subliminal import download_best_subtitles
from subliminal.video import Video

from .movie import Metadata, local_movie


def srt_to_vtt(srt_path: str, vtt_path: str) -> None:
    with (
        open(srt_path, mode="r", encoding="utf-8") as srt,
        open(vtt_path, mode="w", encoding="utf-8") as vtt,
    ):
        vtt.write("WEBVTT\n\n")
        for line in srt:
            vtt.write(line.replace(",", "."))


def download_subtitle(movie_path: str, language: str = "eng") -> None:
    video = Video.fromname(movie_path)
    subtitles = download_best_subtitles([video], {Language(language)})

    subtitle_path = f"{os.path.splitext(movie_path)[0]}sub.srt"

    if video in subtitles:
        subtitle = subtitles[video]

        if subtitle:
            subtitle = subtitle[0]

            print(subtitle_path)
            if subtitle.content is not None:
                with open(subtitle_path, mode="wb") as f:
                    f.write(subtitle.content)
    else:
        with open(subtitle_path, "w", encoding="utf-8") as f:
            f.write("")


def find_movies() -> List[Metadata]:
    movies = []

    for name in os.listdir("./client/public/Data/movies"):
        video = None
        subtitles = False
        path = f"./client/public/Data/movies/{name}"
        for file in os.listdir(path):
            if file.endswith(".mp4"):
                video = f"{path}/{file}"
            if file.endswith(".mkv"):
                video = f"{path}/{file}"
            if file.endswith(".vtt"):
                subtitles = True

        if not subtitles:
            sub_path_prefix = f"./client/public/Data/movies/{name}/"
            download_subtitle(sub_path_prefix)
            srt_to_vtt(f"{sub_path_prefix}sub.srt", f"{sub_path_prefix}sub.vtt")

        if video is not None:
            metadata_path = f"./client/public/Data/movies/{name}/metadata.json"
            if os.path.exists(metadata_path):
                with open(metadata_path, mode="r", encoding="utf-8") as f:
                    metadata = json.load(f)
            else:
                name = name[: name.find("(")] if "(" in name else name
                name = name[: name.find(".")] if "." in name else name
                name = name[: name.find("[")] if "[" in name else name
                name = name.lower().strip()

                metadata = local_movie(name, video)

                with open(metadata_path, mode="w+", encoding="utf-8") as f:
                    json.dump(metadata, f)

            if metadata is not None:
                movies.append(metadata)

    return movies
