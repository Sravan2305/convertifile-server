from enum import Enum


class FileFormats(str, Enum):
    TEXT = 'txt'
    EXCEL = 'xls'
    POWER_POINT = 'ppt'
    WORD = 'doc'
    PDF = 'pdf'
    IMAGE_JPG = 'jpg'
    IMAGE_PNG = 'png'
    IMAGE_JPEG = 'jpeg'


class Possibilities(str, Enum):
    TEXT = [FileFormats.TEXT, FileFormats.EXCEL]
