from fastapi import FastAPI
from pydantic import BaseModel
from app.api import api_router, HTTPException

app = FastAPI(title="Aviation Tech Records API")

# In-memory storage (temporary database)
items = []

class Item(BaseModel):
    name: str

@app.get("/health")
def root():
    return {"message": "Aviation Records System Running"}

@app.post("/items")
def create_item(item: Item):
    items.append(item.name)
    return {"items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id <len(items):
        return {"item": items[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

app.include_router(api_router)
