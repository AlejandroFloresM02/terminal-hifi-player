import os

import miniaudio
from flac_player.music_queue import pop_file
from is_supported_file import is_supported_file


# helpers
def file_exists(file_path: str) -> bool:
    return os.path.exists(file_path)



def print_file_info(info):
    print(f"File: {info.name}")
    print(
        f"Format: {info.file_format.name}, {info.nchannels} channels, {info.sample_rate} Hz, {info.duration:.1f}s"
    )
    print(f"{info.sample_width} bytes per sample: {info.sample_format_name}")


class Player:
    def __init__(self, queue):
        self.queue = queue
        self.history = []
        self.file_path = None
        self.stream = None
        self.device = None
        self.is_paused = False
        self.is_playing = False
        self.is_finished = False

    def play_file(self, file_path) -> bool:
        self.stop()
        self.file_path = file_path
        self.is_paused = False
        self.is_playing = False
        self.is_finished = False

        if not file_exists(self.file_path):
            print("File not found")
            return False

        if not is_supported_file(self.file_path):
            print("Unsupported file type")
            return False

        info = miniaudio.get_file_info(self.file_path)
        try:
            self.stream = miniaudio.stream_file(
                self.file_path,
                output_format=info.sample_format,
                sample_rate=info.sample_rate,
            )
        except miniaudio.MiniaudioError as e:
            print("Cannot create optimal stream: ", e)
            return False

        self.device = miniaudio.PlaybackDevice(
            output_format=info.sample_format,
            sample_rate=info.sample_rate,
        )
        self.device.start(self.stream)
        self.is_playing = True
        return True

    def pause(self):
        if self.device and self.is_playing and not self.is_paused:
            self.device.stop()
            self.is_paused = True

    def resume(self):
        if self.device and self.is_paused:
            self.device.start(self.stream)
            self.is_paused = False

    def stop(self):
        if self.device:
            self.device.stop()
            self.device.close()
            self.device = None
        self.stream = None
        self.is_paused = False
        self.is_playing = False

    def next_file(self) -> bool:
        if not self.queue:
            return False
        previous_path = self.file_path
        if self.file_path:
            self.history.append(self.file_path)
        self.stop()
        file_path = pop_file(self.queue)
        if not self.play_file(file_path):
            self.queue.insert(0, file_path)
            if self.history and self.history[-1] == previous_path:
                self.history.pop()
            return False
        return True

    def previous_file(self) -> bool:
        if not self.history:
            return False
        if self.file_path:
            self.queue.insert(0, self.file_path)
        self.stop()
        file_path = self.history.pop()
        if not self.play_file(file_path):
            self.history.append(file_path)
            return False
        return True
