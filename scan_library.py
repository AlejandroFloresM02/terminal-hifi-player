import os

from flac_player.enums.supported_file_types import SupportedFileTypes


def is_supported_file(filename: str) -> bool:
    extension = os.path.splitext(filename)[1].lower()
    return extension in {file_type.value for file_type in SupportedFileTypes}


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
