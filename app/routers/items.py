from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()

# In-memory store for demo only
_items: dict[int, dict] = {}
_next_id = 1


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: str | None = None


class Item(ItemCreate):
    id: int


@router.get("", response_model=list[Item])
def list_items() -> list[Item]:
    return [Item(**row) for row in _items.values()]


@router.post("", response_model=Item, status_code=201)
def create_item(body: ItemCreate) -> Item:
    global _next_id
    item_id = _next_id
    _next_id += 1
    row = {"id": item_id, "name": body.name, "description": body.description}
    _items[item_id] = row
    return Item(**row)


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**_items[item_id])


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
