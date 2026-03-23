import os

from is_supported_file import is_supported_file


def scan_library(directory: str) -> dict:
    albums = {}  # a dictionary to store albums and their tracks
    for entry in os.listdir(directory):
        album_path = os.path.join(directory, entry)
        if os.path.isdir(album_path):
            tracks = sorted(
                [
                    os.path.join(album_path, file)
                    for file in os.listdir(album_path)
                    if is_supported_file(file)
                ]
            )
            if tracks:
                albums[entry] = tracks
    return albums
