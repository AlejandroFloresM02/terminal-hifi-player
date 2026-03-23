import os

from supported_file_types_enum import SupportedFileTypes


def is_supported_file(filename: str) -> bool:
    extension = os.path.splitext(filename)[1].lower()
    return extension in {file_type.value for file_type in SupportedFileTypes}
