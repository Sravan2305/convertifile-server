import os
from fastapi import BackgroundTasks, APIRouter, UploadFile, HTTPException, responses
from controllers.conversion import file_format_converter
from controllers.multipleFilesConversion import images_to_pdf_converter, multiple_file_format_converter
from models.fileFormats import FileFormats
from utils import zipConverter, emptyDirectory, sendSingleFIle, checkConversion
from typing import List

file_convert_router = APIRouter()


@file_convert_router.post("/convert-single-file")
async def convert(file: UploadFile, to_format: FileFormats, background_tasks: BackgroundTasks):
    if not checkConversion.is_conversion_required(file.filename, to_format):
        return responses.JSONResponse(status_code=200, content={"message": "File already in the required format",
                                                                "conversionRequired": False})
    stored_file_name = await file_format_converter(file, to_format)
    if stored_file_name == "":
        raise HTTPException(status_code=500, detail="Sorry! Something went wrong")
    files = [filename for filename in os.listdir(os.path.join(os.path.dirname(__file__), '../../../results')) if
             filename.startswith(stored_file_name[:32])]
    if len(files) == 0:
        raise HTTPException(status_code=500, detail="Sorry! Something went wrong")
    if len(files) > 1:
        response = zipConverter.zip_files(files, file.filename)
    else:
        response = sendSingleFIle.send_single_file(files[0], to_format)

    # background_tasks.add_task(emptyDirectory.empty_directory)
    return response
    # return {"message": "Convertifile is working on " + file.filename}


@file_convert_router.post("/multiple-files-convert")
async def convert_multiple_files(file: List[UploadFile], to_format: FileFormats, background_tasks: BackgroundTasks):
    stored_folder_name = await multiple_file_format_converter(file, to_format)
    if stored_folder_name == "":
        raise HTTPException(status_code=500, detail="Sorry! Something went wrong")
    background_tasks.add_task(emptyDirectory.empty_directory)
    print(stored_folder_name.split('/')[-1])
    return sendSingleFIle.send_single_file(stored_folder_name.split('/')[-1], to_format)
