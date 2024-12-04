from fastapi import FastAPI, HTTPException
from typing import List
from app.models.item import Item

# Create FastAPI instance
app = FastAPI(title="Item Management API",
             description="A simple FastAPI server for managing items",
             version="1.0.0")

# Simulate a database using a list
items_db = []
counter = 1

@app.get("/")
async def root():
    """Root endpoint returning a welcome message"""
    return {"message": "Welcome to the FastAPI server!"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """Create a new item"""
    global counter
    item.id = counter
    counter += 1
    items_db.append(item)
    return item

@app.get("/items/", response_model=List[Item])
async def get_items():
    """Get all items"""
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get item by ID"""
    item = next((item for item in items_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item"""
    item = next((item for item in items_db if item.id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db.remove(item)
    return {"message": "Item deleted successfully"} 