import os
from fastapi import BackgroundTasks, APIRouter, UploadFile, HTTPException, Response
from controllers.conversion import file_format_converter
from models.fileFormats import FileFormats
from utils import zipConverter, emptyDirectory, sendSingleFIle

file_convert_router = APIRouter()


@file_convert_router.post("/convert-file")
async def convert(file: UploadFile, to_format: FileFormats, background_tasks: BackgroundTasks):
    stored_file_name = await file_format_converter(file, to_format)
    if stored_file_name == "":
        raise HTTPException(status_code=500, detail="Sorry! Something went wrong")
    files = [filename for filename in os.listdir(os.path.join(os.path.dirname(__file__), '../../../results')) if
             filename.startswith(stored_file_name[:32])]
    if len(files) > 1:
        response = zipConverter.zip_files(files, file.filename)
    else:
        response = sendSingleFIle.send_single_file(files[0], to_format)

    background_tasks.add_task(emptyDirectory.empty_directory)
    return response
    # return {"message": "Convertifile is working on " + file.filename}
