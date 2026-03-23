from typing import Annotated

from fastapi import FastAPI, Form, Depends, HTTPException, Request
from pydantic import BaseModel, ValidationError

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str

    model_config = {"extra": "forbid"}


# def get_form_data(
#     username: Annotated[str, Form()],
#     password: Annotated[str, Form()],
# ) -> FormData:
#     try:
#         return FormData(username=username, password=password)
#     except ValidationError as e:
#         raise HTTPException(status_code=422, detail=e.errors())


async def get_form_data(request: Request) -> FormData:
    form = await request.form()
    data = dict(form)

    try:
        return FormData(**data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username}


@app.post("/login/")
async def login(data: FormData = Depends(get_form_data)):
    return data
