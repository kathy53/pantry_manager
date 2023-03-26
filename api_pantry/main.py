"""
Sources:
https://www.datacamp.com/tutorial/introduction-fastapi-tutorial
FastAPI Introduction - Build Your First Web App - Python Tutorial
"""

from typing import Union 
from fastapi import FastAPI 
app = FastAPI()

@app.get("/")

def read_root():
    return{"Hello": "World"}


@app.get("/items/{item_id}")

def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}