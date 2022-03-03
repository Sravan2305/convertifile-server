import os.path
import uuid
import pytesseract
from PIL import Image
from fastapi import UploadFile
from pdf2image import convert_from_path
from models.fileFormats import FileFormats
import os
import shutil

"""
A controller which converts a file to a different format.
@:param :file Request Obj
@:returns: Response Obj
"""


async def file_format_converter(file: UploadFile, to_format: FileFormats) -> str:
    # Storing the file in a temporary location
    unique_id = uuid.uuid4()
    if save_file(file, str(unique_id)):
        # file name sent to the transformer = unique_id + file name
        try:
            await transform_file(str(unique_id) + str(file.filename), to_format)
            return str(unique_id) + str(file.filename)
        except:
            return ""


"""
A controller which converts a file to a different format.
@:param :fileName, to_format
@actions : save a fie in results folder with 
    file_name = fileLocation without extension (uuid+filename) + toFormat (extension)
@:returns: bool
"""


async def transform_file(filename: str, to_format: FileFormats):
    filename_without_extension, extension_with_dot = os.path.splitext(filename)
    from_format = extension_with_dot[1:]
    file_location = f"files/{filename}"

    if to_format == FileFormats.TEXT:
        """
              TEXT CONTROLLER
        """
        if [FileFormats.JPG, FileFormats.PNG, FileFormats.JPEG].__contains__(from_format):
            saved_file_location = f"results/{filename_without_extension + f'.{to_format}'}"
            pytesseract.pytesseract.tesseract_cmd = f'OCR-Packs/tesseract.exe'
            useropfile = open(saved_file_location, 'a')
            text = str((pytesseract.image_to_string(Image.open(file_location))))
            useropfile.write(text)
            useropfile.close()
    elif [FileFormats.JPG, FileFormats.PNG, FileFormats.JPEG].__contains__(to_format):
        """
              IMAGE CONTROLLER
        """
        if from_format == 'pdf':
            pages = convert_from_path(file_location, 500, poppler_path=f'extpacks/poppler-0.68.0/bin')
            count = 0
            for page in pages:
                useropfile = f"results/{filename_without_extension + str(count) + f'.{to_format}'}"
                page.save(useropfile, 'JPEG')
                count += 1
        elif [FileFormats.JPG, FileFormats.PNG, FileFormats.JPEG].__contains__(from_format):
            print(filename)
            file_path = os.path.join("files/", filename)
            shutil.copy(file_path, os.path.join("results/"))
            os.rename("results/" + filename, "results/" + filename_without_extension + f'.{to_format}')
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
    try:
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
            return True
    except:
        return False
