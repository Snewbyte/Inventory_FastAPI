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

Products = [{'ID': 0, 'Name': 'Apple', 'Price': 4.99, 'Type': 'Fruit'},
            {'ID': 1, 'Name': 'Orange', 'Price': 8.99, 'Type': 'Fruit'},
            {'ID': 2, 'Name': 'Tomato', 'Price': 3.99, 'Type': 'Fruit'},
            {'ID': 3, 'Name': 'Cabbage', 'Price': 1.99, 'Type': 'Vegetable'},
            {'ID': 4, 'Name': 'Potato', 'Price': 2.50, 'Type': 'Vegetable'},
            {'ID': 5, 'Name': 'Carrots', 'Price': 1.49, 'Type': 'Vegetable'}]

#uvicorn main:app --reload

from fastapi import FastAPI
#from typing import Union
from pydantic import BaseModel

app = FastAPI(title = "Module 3 API",
              version = "0.0.2",
              contact = {"name": "Samuel Newbold", "email": "srnewbold17955@mail.mccneb.edu"},
              description = "Introducing POST and swagger to API for assignment 3"
              )


class Product(BaseModel):
    ID: int
    Name: str
    Price: float
    Type: str


@app.get("/products")
def get_all_products():
    return Products

@app.post("/products/mod")
def update_product(product : Product):
    for existing_product in Products:
        if existing_product["ID"] == product.ID:        # if product already exists modify it
                existing_product["Name"] = product.Name
                existing_product["Price"] = product.Price
                existing_product["Type"] = product.Type
                return f"Modified product"

    new_product = {"ID": product.ID,                    # if product doesn't exist create new product
                   "Name": product.Name,
                   "Price": product.Price,
                   "Type": product.Type
                   }

    Products.append(new_product)                        # append dictionary
    return f"Added new product"