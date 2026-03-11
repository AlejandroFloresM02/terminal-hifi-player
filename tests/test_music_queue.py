import unittest

from flac_player import music_queue
from flac_player.music_queue import (
    add_file,
    move_file_queue_location,
    peek_file,
    pop_file,
)


class TestMusicQueue(unittest.TestCase):
    def test_add_file(self):
        music_queue = []
        add_file(music_queue, "test_file.flac")
        self.assertEqual(music_queue[0], "test_file.flac")

    def test_move_file_queue_location(self):
        music_queue = ["file1.flac", "file2.flac", "file3.flac"]
        move_file_queue_location(music_queue, 1, 2)
        self.assertEqual(music_queue, ["file1.flac", "file3.flac", "file2.flac"])

    def test_peek_file(self):
        music_queue = ["file1.flac", "file2.flac", "file3.flac"]
        self.assertEqual(peek_file(music_queue), "file1.flac")

    def test_pop_file(self):
        music_queue = ["file1.flac", "file2.flac", "file3.flac"]
        self.assertEqual(pop_file(music_queue), "file1.flac")
        self.assertEqual(music_queue, ["file2.flac", "file3.flac"])

    def test_failed_pop_file(self):
        music_queue = []
        self.assertFalse(pop_file(music_queue))

    def test_failed_peek(self):
        music_queue = []
        self.assertFalse(peek_file(music_queue))

    def test_failed_move_invalid_new_index(self):
        music_queue = ["file1.flac", "file2.flac", "file3.flac"]
        result = move_file_queue_location(music_queue, 1, 4)
        self.assertFalse(result)
        self.assertEqual(music_queue, ["file1.flac", "file2.flac", "file3.flac"])

    def test_failed_move_invalid_old_index(self):
        music_queue = ["file1.flac", "file2.flac", "file3.flac"]
        result = move_file_queue_location(music_queue, 4, 2)
        self.assertFalse(result)
        self.assertEqual(music_queue, ["file1.flac", "file2.flac", "file3.flac"])
