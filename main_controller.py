from fastapi import FastAPI, HTTPException, status
from databases import Database

from modules.product_module import Product, ProductRequest, ProductTypeEnum, ResponseMessage
from services.main_service import get_product_by_id_query, get_all_products_query, convert_data_to_module, insert_new_product_query, update_product_query, get_products_price_range_query, search_products_query
from typing import List, Union
app = FastAPI(title='Module 6 API',
              version="0.0.5",
              contact={'name': 'Samuel Newbold', 'email': 'srnewbold17955@mail.mccneb.edu'},
              description='Fast API with 200 and 400 responses')

database = Database("sqlite:///services/main.db")


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


##################### POST #####################
@app.post("/products/mod/")
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
@app.get("/product", response_model=Product, responses={200:{"model":Product},400:{"model":ResponseMessage}})
async def get_product(product_id: int) -> Product:

    results = await database.fetch_all(get_product_by_id_query(product_id))
    if len(results) == 0:       # if id isn't valid query will return a empty list
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product ID not found")

  # since convert_data_to_module returns a list we just need to return index 0
    return convert_data_to_module(results)[0]

@app.get("/products", response_model=List[Product])
async def get_all_products():
    results = await database.fetch_all(get_all_products_query())
    if len(results) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No products found")

    return convert_data_to_module(results)

@app.get("/products/price", response_model=List[Product])
async def get_products_price_range(min_price: float, max_price: float):
    results = await database.fetch_all(get_products_price_range_query(min_price, max_price))

    return convert_data_to_module(results)

@app.get("/products/search", response_model=List[Product])
async def search_products(product_price: Union[float, None] = None, product_type: Union[ProductTypeEnum, None] = None):
    results = await database.fetch_all(search_products_query(product_price, product_type))

    return convert_data_to_module(results)

