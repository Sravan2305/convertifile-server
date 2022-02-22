import uuid

import pytesseract
from PIL import Image
from fastapi import UploadFile
from pdf2image import convert_from_path

from models.fileFormats import FileFormats

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
    converted_location = file_location[:-3]
    file_location = f"files/{file_location}"

    ########################################################################################################################
    if to_format == FileFormats.TEXT:
        if file_location[-3:] == 'jpg':
            converted_location = f"results/{converted_location + 'txt'}"
            pytesseract.pytesseract.tesseract_cmd = f'OCR-Packs/tesseract.exe'
            useropfile = open(converted_location, 'a')
            text = str(((pytesseract.image_to_string(Image.open(file_location)))))
            useropfile.write(text)
            useropfile.close()
        pass
    ########################################################################################################################

    elif to_format == FileFormats.IMAGE_JPG:
        if file_location[-3:] == 'pdf':
            pages = convert_from_path(file_location, 500, poppler_path=f'extpacks/poppler-0.68.0/bin')
            count = 0
            for page in pages:
                useropfile = f"results/{converted_location + str(count) + '.jpg'}"
                page.save(useropfile, 'JPEG')
                count += 1
        pass

    ########################################################################################################################
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
