from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Initialize FastAPI app
app = FastAPI(
    title="Sample FastAPI Application",
    description="A simple FastAPI project with basic endpoints",
    version="1.0.0"
)

# Pydantic model for request body
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

# Sample items database
items_db = []

@app.get("/")
async def root():
    """Root endpoint that returns a welcome message"""
    return {"message": "Welcome to FastAPI Sample Project!"}

@app.get("/items")
async def get_items():
    """Get all items from the database"""
    return {"items": items_db}

@app.post("/items", status_code=201)
async def create_item(item: Item):
    """Create a new item"""
    items_db.append(item)
    return {"message": "Item created successfully", "item": item}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """Get a specific item by ID"""
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )
    return {"item": items_db[item_id]} 