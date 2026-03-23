Products = [{'ID': 0, 'Name': 'Apple', 'Price': 4.99, 'Type': 'Fruit'},
            {'ID': 1, 'Name': 'Orange', 'Price': 8.99, 'Type': 'Fruit'},
            {'ID': 2, 'Name': 'Tomato', 'Price': 3.99, 'Type': 'Fruit'},
            {'ID': 3, 'Name': 'Cabbage', 'Price': 1.99, 'Type': 'Vegetable'},
            {'ID': 4, 'Name': 'Potato', 'Price': 2.50, 'Type': 'Vegetable'},
            {'ID': 5, 'Name': 'Carrots', 'Price': 1.49, 'Type': 'Vegetable'}]

#uvicorn main:app --reload

from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI(title = "Module 3 API",
              version = "0.0.2",
              contact = {"name": "Samuel Newbold", "email": "srnewbold17955@mail.mccneb.edu"},
              description = "Introducing POST and swagger to API for assignment 3")


class Product(BaseModel):
    ID: int
    Name: str
    Price: float
    Type: str


@app.get("/products")
def get_all_products():
    return Products