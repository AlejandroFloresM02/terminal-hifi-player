import os
import tempfile
import unittest

from scan_library import scan_library


class TestScanLibrary(unittest.TestCase):
    def test_scan_library(self):
        self.temp_dir = tempfile.mkdtemp()
        self.album_path = os.path.join(self.temp_dir, "Artist - Album")
        os.makedirs(self.album_path)
        for name in ["01 Track A.flac", "02 Track B.flac"]:
            open(os.path.join(self.album_path, name), "w").close()

        def test_finds_album(self):
            albums = scan_library(self.temp_dir)
            self.assertIn("Artist - Album", albums)

        def test_finds_tracks(self):
            albums = scan_library(self.temp_dir)
            self.assertEqual(len(albums["Artist - Album"]), 2)

        def test_ignores_non_supported_files(self):
            open(os.path.join(self.album.path, "cover.jpg"), "w").close()
            albums = scan_library(self.temp_dir)
            self.assertEquat(len(albums["Artist - Album"]), 2)

        def test_ignores_empty_album(self):
            empty_album = os.path.join(self.temp_dir, "Empty Album")
            os.makedirs(empty_album)
            albums = scan_library(self.temp_dir)
            self.assertNotIn("Empty Album", albums)

        def test_empty_directory(self):
            empty_dir = tempfile.mkdtemp()
            albums = scan_library(empty_dir)
            self.assertEqual(albums, {})
