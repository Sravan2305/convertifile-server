from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.api import api_router
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title=env["PROJECT_NAME"],
    description="Converti-File is a simple file converter to convert files to other formats online for free.",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    docs_version="0.1.0",
)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hi there! Thanks for visiting Convertifile :)."}


app.include_router(api_router, prefix=env["V1_PREFIX"])
