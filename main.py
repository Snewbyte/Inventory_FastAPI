Products = [{'Name': 'Apple', 'Price': 4.99, 'Type': 'Fruit'},
            {'Name': 'Orange', 'Price': 8.99, 'Type': 'Fruit'},
            {'Name': 'Tomato', 'Price': 3.99, 'Type': 'Fruit'},
            {'Name': 'Cabbage', 'Price': 1.99, 'Type': 'Vegetable'},
            {'Name': 'Potato', 'Price': 2.50, 'Type': 'Vegetable'}]

#uvicorn main:app --reload

from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/product") #product endpoint
def get_products(product_price: float, product_type: Union[str, None] = None, product_name: Union[str, None] = None):
    return ["Hello World"]

@app.get("/product/price")
def get_all_products_price_range(min_price: float, max_price: float):
    return ["Hello World"]