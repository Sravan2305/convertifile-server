from fastapi import APIRouter, UploadFile

file_convert_router = APIRouter()


@file_convert_router.post("/convert-file")
async def convert(file: UploadFile):
    fileFormatConverter(file)
    return {"message": "Convertifile is working on " + file.filename}
