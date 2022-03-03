from typing import List
from fastapi import UploadFile
from models.fileFormats import FileFormats
from uuid import uuid4
from utils import saveAFile
from PIL import Image
import os


async def multiple_file_format_converter(files_list: List[UploadFile], to_format: FileFormats) -> str:
    unique_id = str(uuid4())
    file_counter = 0
    # if folder is not created, new file cannot be saved in imaginary folder
    os.makedirs(f"files/{unique_id}")
    for file in files_list:
        file_counter += 1
        if not saveAFile.save_file(file, f"files/{unique_id}/{file_counter}"):
            return ""
    try:
        return await transform_files(f"files/{unique_id}", to_format)
    except:
        return ""


async def transform_files(folder_path: str, to_format: FileFormats) -> str:
    from_format = os.listdir(folder_path)[0].split(".")[-1]
    results_path = f"results/{uuid4()}{os.listdir(folder_path)[0].split('.')[0]}.pdf"
    if to_format == FileFormats.PDF:
        if [FileFormats.PNG, FileFormats.JPG, FileFormats.JPEG].__contains__(from_format):
            images_list = [Image.open(f"{folder_path}/{file}") for file in os.listdir(folder_path)]
            images_list[0].save(
                results_path, "PDF", resolution=100.0, save_all=True, append_images=images_list[1:]
            )
            print(results_path)
            return results_path
    return ""


async def images_to_pdf_converter(images_list, pdf_name):
    pass
