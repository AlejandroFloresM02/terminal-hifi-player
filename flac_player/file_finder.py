import argparse
import os

import numpy as np

from flac_player.supported_file_types import SupportedFileTypes


def find_audio_file(directory: str):
    queue_array = np.array([])
    files = os.listdir(directory)
    for file in files:
        if file.endswith(SupportedFileTypes.FLAC.value) or file.endswith(
            SupportedFileTypes.MP3.value
        ):
            queue_array = np.append(queue_array, os.path.join(directory, file))
            print(f"[DEBUG] {queue_array}")
            return queue_array
    return False


def load_file():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Directory to search for audio files")
    args = parser.parse_args()

    if find_audio_file(args.directory):
        print("[DEBUG] Audio file found!")
    else:
        print("[DEBUG] No audio file found.")
