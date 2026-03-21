from typing import Literal

from fastapi import FastAPI, Depends, Request, HTTPException
from pydantic import BaseModel, Field, ValidationError

app = FastAPI()


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at", "name"] = "created_at"
    tags: list[str] = Field(default_factory=list)


# ✅ strict validator dependency
async def get_filter_params(request: Request) -> FilterParams:
    query_dict = dict(request.query_params)

    try:
        return FilterParams(**query_dict)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@app.get("/items")
async def read_items(filter_query: FilterParams = Depends(get_filter_params)):
    return filter_query
