from fastapi import UploadFile
from models.fileFormats import FileFormats
import uuid

"""
A controller which converts a file to a different format.
@:param :file Request Obj
@:returns: Response Obj
"""


async def file_format_converter(file: UploadFile, to_format: FileFormats) -> UploadFile:
    # Storing the file in a temporary location
    unique_id = uuid.uuid4()
    if save_file(file, str(unique_id)):
        # file name sent to the transformer = unique_id + file name
        transform_file(str(unique_id) + str(file.filename), to_format)
    return file


"""
A controller which converts a file to a different format.
@:param :fileName, to_format
@actions : save a fie in results folder with 
    file_name = fileLocation without extension (uuid+filename) + toFormat (extension)
@:returns: bool
"""


def transform_file(file_location: str, to_format: FileFormats):
    if to_format == FileFormats.TEXT:
        # Bhargav TODO
        pass
    elif to_format == FileFormats.PDF:
        # Bhargav TODO
        pass
    else:
        return False
    return True


"""
A controller which converts a file to a different format.
@:param :file Request Obj , unique_id
@:returns: bool
"""


def save_file(file: UploadFile, uid: str):
    file_location = f"files/{uid}{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return True
