from enum import Enum


class FileFormats(str, Enum):
    TEXT = 'txt'
    EXCEL = 'xls'
    POWER_POINT = 'ppt'
    WORD = 'doc'
    PDF = 'pdf'
    JPG = 'jpg'
    PNG = 'png'
    JPEG = 'jpeg'


class Possibilities(str, Enum):
    TEXT = [FileFormats.TEXT, FileFormats.EXCEL]
