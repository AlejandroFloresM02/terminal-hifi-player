import os

import miniaudio
from supported_file_types import SupportedFileTypes


def file_exists(file_path: str) -> bool:
    return os.path.exists(file_path)


def is_supported(file_path: str) -> bool:
    extension = "." + file_path.split(".")[-1].lower()
    return extension in {file_type.value for file_type in SupportedFileTypes}


def play_file(file_path: str):
    if not file_exists(file_path):
        print("File not found")
        return

    if not is_supported(file_path):
        print("Unsupported file type")
        return

    info = miniaudio.get_file_info(file_path)
    # print_file_info(info) - Debug print
    try:
        stream = miniaudio.stream_file(
            file_path, output_format=info.sample_format, sample_rate=info.sample_rate
        )
    except miniaudio.MiniaudioError as e:
        print("Cannot create optimal stram: ", e)
        return

    with miniaudio.PlaybackDevice(
        output_format=info.sample_format,
        sample_rate=info.sample_rate,
    ) as device:
        device.start(stream)
        input("Press Enter to stop playback: ")


def print_file_info(info):
    print(f"File: {info.name}")
    print(
        f"Format: {info.file_format.name}, {info.nchannels} channels, {info.sample_rate} Hz, {info.duration:.1f}s"
    )
    print(f"{info.sample_width} bytes per sample: {info.sample_format_name}")
