import os
from genericpath import exists


def add_file(music_queue: list, file_path: str):
    music_queue.append(file_path)
    return True


def move_file_queue_location(music_queue: list, old_index: int, new_index: int):
    if old_index < 0 or old_index >= len(music_queue):
        print("Invalid old index")
        return False
    if new_index < 0 or new_index >= len(music_queue):
        print("Invalid new index")
        return False
    try:
        temp = music_queue.pop(old_index)
        music_queue.insert(new_index, temp)
    except Exception as e:
        print("Error moving file in queue")
        print(f"Error message: {str(e)}")
        return False
    return True


def pop_file(music_queue: list):
    if len(music_queue) <= 0:
        return False
    try:
        temp = music_queue.pop(0)
    except Exception as e:
        print("Error popping file from queue")
        print(f"Error message: {str(e)}")
        return False
    return temp


def peek_file(music_queue: list):
    if len(music_queue) <= 0:
        return False
    return music_queue[0]
