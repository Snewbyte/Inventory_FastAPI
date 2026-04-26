from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from databases import Database

from modules.product_module import Product, ProductRequest, ResponseMessage
from services.main_service import get_product_by_id_query, get_all_products_query, convert_data_to_module, insert_new_product_query, update_product_query, get_products_price_range_query, search_products_query
from typing import List, Union
app = FastAPI(title='Module 8 API',
              version="0.0.7",
              contact={'name': 'Samuel Newbold', 'email': 'srnewbold17955@mail.mccneb.edu'},
              description='Implementing Unit Tests in FastAPI',)

# setting up middleware that helps validate headers
origins = ["*"]
app.add_middleware( CORSMiddleware,
                    allow_origins = origins,
                    allow_credentials = True,
                    allow_methods = ["*"],
                    allow_headers = ["*"],)

database = Database("sqlite:///services/main.db")

tokens = ["abcdefg"]
# tokens stored in api and when a user calls your endpoints they pass tokens in the header

# generate token in database -> give to user -> user makes api call -> check for token and increment token counter for that user

# header comes in key value format

# we will make another table that contains a few tokens and keep them in an array
# check if token is passed through header and check if it is active
# if it is we return an object
# if not we return not authorized status code
# make sure swagger has updated status codes

# "request" object vs request object
# "request" object is something that is sent by the website to the api and contains information about the sender including headers
# request object is and object developers define for passing data to the endpoint (ProductRequest in our case)

@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


##################### POST #####################
@app.post("/products/mod/", responses={200:{"model": str}, 400: {"model": ResponseMessage}, 401:{"model": ResponseMessage}})
async def modify_product(product: ProductRequest, request: Request):
    # check empty fields
    if product.Name == "" or product.Type == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name or type cannot be empty")

    results = await database.fetch_all(get_product_by_id_query(product.ID))  # Getting a product by id, will yield at least one if data exist
    message = "" # create outside of if to use

    print(request.headers["Authorization"]) #if you want to see the full header remove ["Authorization"]
    if request.headers["Authorization"] not in tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized Request")
    if len(results) > 0: # call the update as we found one
        await database.execute(update_product_query(product))  #  We are passing update product query from main_service
        message = "Successfully updated product"
    else: # nothing found so add new product
        await database.execute(insert_new_product_query(product))  #  No data was found, we need to insert new data
        message = "Successfully added a new product"

    return message


##################### GET #####################
@app.get("/product", response_model=Product, responses={200:{"model":str},400:{"model":ResponseMessage}})
async def get_product(product_id: int) -> Product:

    results = await database.fetch_all(get_product_by_id_query(product_id))
    if len(results) == 0:       # if id isn't valid query will return a empty list
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product ID not found")

  # since convert_data_to_module returns a list we just need to return index 0
    return convert_data_to_module(results)[0]

@app.get("/products", response_model=List[Product], responses={200:{"model":List[Product]},400:{"model":ResponseMessage}})
async def get_all_products():

    results = await database.fetch_all(get_all_products_query())
    if len(results) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No products found")

    return convert_data_to_module(results)

@app.get("/products/price", response_model=List[Product], responses={200:{"model":List[Product]},400:{"model":ResponseMessage}})
async def get_products_price_range(min_price: float, max_price: float):

    results = await database.fetch_all(get_products_price_range_query(min_price, max_price))
    if len(results) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No products found in that range")

    return convert_data_to_module(results)

@app.get("/products/search", response_model=List[Product], responses={200:{"model":List[Product]},400:{"model":ResponseMessage}})
async def search_products(product_price: Union[float, None] = None, product_type: Union[str, None] = None):

    results = await database.fetch_all(search_products_query(product_price, product_type))
    if len(results) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No products found with that criteria")

    return convert_data_to_module(results)

