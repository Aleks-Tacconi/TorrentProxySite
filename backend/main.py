import os
import shutil
import threading
from datetime import timedelta

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    exceptions,
    verify_jwt_in_request,
)
from torrent_sites import TorrentStore
from utils import download, find_movies, movie_metadata, torrent

from backend.torrent_sites.torrent_site import SearchResult

USERS = {"admin": "secret"}

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["JWT_SECRET_KEY"] = "ajkflajsdf93wjf328hfD734"

CORS(app, resources={r"/api/*": {"origins": "*"}})
jwt = JWTManager(app)

torrent_store = TorrentStore()


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if USERS.get(username) == password:
        access_token = create_access_token(
            identity=username, expires_delta=timedelta(days=7)
        )
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Invalid credentials"}), 401


@app.before_request
def check_jwt():
    public_paths = ["/api/login"]
    if any(request.path.startswith(p) for p in public_paths):
        return

    try:
        verify_jwt_in_request()
    except exceptions.NoAuthorizationError:
        return jsonify({"redirect": "/login"}), 401


@app.route("/api/movies")
def movies():
    query = request.args.get("query")

    if query is None:
        return jsonify({})

    results = torrent_store.search(query)
    new_results = []

    for result in results:
        if result not in new_results:
            new_results.append(result)

    return jsonify({"data": new_results})


@app.route("/api/metadata")
def metadata():
    title = request.args.get("title")
    torrent_access_point = request.args.get("link")
    key = request.args.get("id")

    if title is None or key is None or torrent_access_point is None:
        return jsonify({})

    moviemetadata = movie_metadata(
        SearchResult(
            title=title,
            torrent_access_point=torrent_access_point,
            id=key,
        )
    )

    return jsonify({"data": moviemetadata})


@app.route("/api/torrents")
def torrents():
    link = request.args.get("link")
    key = request.args.get("key")

    if key is None or link is None:
        return jsonify({})

    torrents_lst = torrent_store.get_torrents(key, link)

    return jsonify({"data": torrents_lst})


@app.route("/api/download")
def download_file():
    link = request.args.get("link")
    name = request.args.get("name")

    if link is not None and name is not None:

        def task():
            file = download(link)
            torrent(file)
            shutil.move(
                f"./client/public/Data/downloading/{name}",
                "./client/public/Data/movies/",
            )
            shutil.move(file, f"./client/public/Data/movies/{name}")
            find_movies()

        thread = threading.Thread(target=task)
        thread.start()

    return jsonify({})


@app.route("/api/local")
def local():
    movies_lst = find_movies()
    return jsonify({"data": movies_lst})


@app.route("/api/videos/<filepath>")
def serve_video(filepath):
    filepath = filepath.replace("__", "/")[1:]

    if filepath.startswith("."):
        filepath = filepath[1:]

    full_path = f"{os.getcwd()}{filepath}"

    return send_file(full_path, "video/mp4")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
