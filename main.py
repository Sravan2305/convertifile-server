from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hi there! Thanks for visiting Convertifile :)."}
