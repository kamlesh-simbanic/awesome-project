from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    # url: str
    url: HttpUrl | None = None
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    # tags: list[str] = []
    tags: set[str] = set()

    # image: Image | None = None
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# Deeply nested models


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


# Bodies of pure lists
@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images
