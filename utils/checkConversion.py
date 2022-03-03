from models import fileFormats
import os

"""
CHeck if conversion can be handled
"""


def is_conversion_possible(current: str, to: str) -> bool:
    pass


def is_conversion_required(current: str, to: str) -> bool:
    filename_without_extension, extension_with_dot = os.path.splitext(current)
    from_format = extension_with_dot[1:]
    if from_format == to:
        return False
    return True
