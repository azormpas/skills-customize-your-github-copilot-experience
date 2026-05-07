from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items = {}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI assignment"}

@app.post("/items/")
async def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, "item": item}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        return {"error": "Item not found"}
    return {"id": item_id, "item": item}
