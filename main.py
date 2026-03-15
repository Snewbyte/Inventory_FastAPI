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
    results = []

    for product in Products:
        if product["Price"] != product_price: #if prices don't match then skip
            continue

        if product_type is not None and product["Type"] != product_type:  #if product type isn't none and doesn't match then skip
            continue

        if product_name is not None and product["Name"] != product_name:  #if product name isn't none and doesn't match then skip
            continue

        results.append(product) #put results in list

    return results #return list




@app.get("/product/price")
def get_all_products_price_range(min_price: float, max_price: float):
    results = []

    for product in Products:
        if min_price < product["Price"] < max_price:
            results.append(product)

    return results