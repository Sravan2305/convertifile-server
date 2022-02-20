from fastapi import APIRouter, UploadFile
from controllers.conversion import file_format_converter
from models.fileFormats import FileFormats

file_convert_router = APIRouter()


@file_convert_router.post("/convert-file")
async def convert(file: UploadFile, to_format: FileFormats):
    new_file = await file_format_converter(file, to_format)
    return {"message": "Convertifile is working on " + file.filename}
