from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


class Tags(Enum):
    items = "items"
    users = "users"


# @app.post("/items/", status_code=status.HTTP_201_CREATED)
# async def create_item(item: Item) -> Item:
#     return item

# Tags
# @app.post("/items/", tags=["items"])
# async def create_item(item: Item) -> Item:
#     return item


# @app.get("/items/", tags=["items"])
# async def read_items():
#     return [{"name": "Foo", "price": 42}]


# @app.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "johndoe"}]


# Tags with Enums
# @app.get("/items/", tags=[Tags.items])
# async def get_items():
#     return ["Portal gun", "Plumbus"]


# @app.get("/users/", tags=[Tags.users])
# async def read_users():
#     return ["Rick", "Morty"]


# Summary and description¶
# @app.post(
#     "/items/",
#     summary="Create an item",
#     description="Create an item with all the information, name, description, price, tax and a set of unique tags",
# )
# async def create_item(item: Item) -> Item:
#     return item


# Description from docstring
# @app.post("/items/", summary="Create an item")
# async def create_item(item: Item) -> Item:
#     """
#     Create an item with all the information:

#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item


# Response description
# @app.post(
#     "/items/",
#     summary="Create an item",
#     response_description="The created item",
# )
# async def create_item(item: Item) -> Item:
#     """
#     Create an item with all the information:

#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item


# Deprecate a path operation
@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
