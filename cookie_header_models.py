from fastapi import FastAPI, Request, Depends, HTTPException
from pydantic import BaseModel, ValidationError

app = FastAPI()


class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


class CommonHeaders(BaseModel):
    # model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


async def get_cookies(request: Request) -> Cookies:
    raw_cookies = request.cookies

    try:
        return Cookies(**raw_cookies)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


async def get_headers(request: Request) -> CommonHeaders:
    try:
        return CommonHeaders(**request.headers)
    except ValidationError as e:
        raise HTTPException(status_code=403, detail=e.errors())


@app.get("/items/")
async def read_items(cookies: Cookies = Depends(get_cookies)):
    return cookies


@app.get("/items/")
async def read_items(headers: CommonHeaders = Depends(get_headers)):
    return headers
