from fastapi import APIRouter
from api.v1.endpoints import convert

api_router = APIRouter()

api_router.include_router(convert.file_convert_router, prefix="/convert", tags=["File Conversion"])
