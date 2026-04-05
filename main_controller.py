from fastapi import FastAPI
from databases import Database

from modules.product_module import Product, ProductRequest
from services.main_service import get_product_by_id_query, get_all_products_query, convert_data_to_module, insert_new_product_query, update_product_query, get_products_price_range_query, search_products_query
from typing import List
app = FastAPI(title='Module 4 API',
              version="0.0.2",
              contact={'name': 'Samuel Newbold', 'email': 'srnewbold17955@mail.mccneb.edu'},
              description='Fast API with databases')

database = Database("sqlite:///services/main.db")


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


##################### POST #####################
@app.post("/product/mod/")
async def modify_product(product: ProductRequest):
    results = await database.fetch_all(get_product_by_id_query(product.ID))  # Getting a product by id, will yield at least one if data exist
    message = "" # create outside of if to use

    if len(results) > 0: # call the update as we found one
        await database.execute(update_product_query(product))  #  We are passing update product query from main_service
        message = "Successfully updated product"
    else: # nothing found so add new product
        await database.execute(insert_new_product_query(product))  #  No data was found, we need to insert new data
        message = "Successfully added a new product"

    return message


##################### GET #####################
@app.get("/products", response_model=List[Product])
async def get_product(product_id: int) -> Product:
    results = await database.fetch_all(get_product_by_id_query(product_id))

    # since convert_data_to_module returns a list we just need to return index 0
    return convert_data_to_module(results)[0]


@app.get("/product/all", response_model=List[Product])
async def get_all_products():
    results = await database.fetch_all(get_all_products())

    return convert_data_to_module(results)

@app.get("/products/prices", response_model=List[Product])
async def get_products_price_range(min_price: float, max_price: float):
    results = await database.fetch_all(get_products_price_range_query(min_price, max_price))
    return convert_data_to_module(results)