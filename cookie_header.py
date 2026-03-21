from typing import Annotated

from fastapi import Cookie, FastAPI, Header

app = FastAPI()


# Cookies
@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}


# Headers
@app.get("/items/")
async def read_items(
    access_token: Annotated[str | None, Header()] = None,
    strange_header: Annotated[str | None, Header(convert_underscores=True)] = None,
    x_token: Annotated[list[str] | None, Header()] = None,
):
    return {
        "access-token": access_token,
        "strange-header": strange_header,
        "x-token": x_token,
    }
