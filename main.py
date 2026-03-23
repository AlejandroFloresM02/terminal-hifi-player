import os

from flac_player.player import Player
from flac_player.enums.player_commands import Command
from scan_library import scan_library


def show_welcome_message():
    print("================================")
    print("  Terminal HiFi Player")
    print("================================")


def show_albums(albums: dict):
    print("\nAvailable albums:")
    for i, album_name in enumerate(albums, 1):
        track_count = len(albums[album_name])
        print(f" {i}. {album_name} ({track_count} tracks)")
    print("\nType 'exit' to quit the program.")


def select_album(albums: dict) -> str | None:
    album_names = list(albums.keys())
    while True:
        choice = input("Select an album (number) or 'exit' to quit: ").strip().lower()
        if choice == "exit":
            return None
        try:
            index = int(choice) - 1
            if 0 <= index < len(album_names):
                return album_names[index]
        except ValueError:
            pass
        print(f"Please enter a number between 1 and {len(album_names)}")


def get_track_name(file_path: str) -> str:
    return os.path.splitext(os.path.basename(file_path))[0]


def show_now_playing(player: Player):
    if player.file_path:
        print(f"\nNow Playing: {get_track_name(player.file_path)}")
        print("Commands: [n]next, [p]previous, [pause], [resume], [q]quit")


def main():
    library_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "music_library"
    )
    albums = scan_library(library_path)
    while True:
        show_welcome_message()
        show_albums(albums)
        album_name = select_album(albums)
        if album_name is None:
            break
        tracks = albums[album_name]

        print(f"\nLoaded: {album_name}\n")

        player = Player(tracks.copy())
        player.next_file()
        show_now_playing(player)
        while True:
            user_input = input("> ").strip().lower()
            try:
                command = Command(user_input)
            except ValueError:
                print(
                    "Invalid command. Type 'q' to quit, 'n' to next, 'p' to previous, 'pause' to pause, 'resume' to resume."
                )
                continue
            match command:
                case Command.QUIT:
                    player.stop()
                    break
                case Command.EXIT:
                    player.stop()
                    return
                case Command.NEXT:
                    player.next_file()
                    show_now_playing(player)
                case Command.PREVIOUS:
                    player.previous_file()
                    show_now_playing(player)
                case Command.PAUSE:
                    player.pause()
                case Command.RESUME:
                    player.resume()


if __name__ == "__main__":
    main()
