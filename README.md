# Terminal HiFi Player

Python program that allows you to select and play local music albums in your terminal.

## Usage

```bash
python main.py
```

## Music Library

Place your music files in the `music_library` folder with the following structure:

```
music_library/
├── album_name/
│   ├── 01_track_title.flac
│   ├── 02_track_title.flac
│   └── ...
```

## Commands

During playback:

| Command  | Action             |
|----------|--------------------|
| `n`      | Next track         |
| `p`      | Previous track     |
| `pause`  | Pause playback     |
| `resume` | Resume playback    |
| `q`      | Back to album list |
| `exit`   | Exit the program   |

Type `exit` at the album selection menu to quit the program.
