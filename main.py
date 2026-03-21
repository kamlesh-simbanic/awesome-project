from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
