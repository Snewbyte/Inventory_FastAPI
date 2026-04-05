from fastapi import FastAPI
from databases import Database

from modules.user_module import User, UserRequest
from services.main_service import get_user_by_id_query, get_all_users_query, convert_data_to_module, insert_new_user, update_user

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



@app.post("/user/mod/")
async def modify_user(user: UserRequest):
    results = await database.fetch_all(get_user_by_id_query(user.ID))  # Getting a user by id, will yield at least one if data exist
    message = "" # create outside of if to use

    if len(results) > 0: # call the update as we found one
        await database.execute(update_user(user))  #  We are passing update user query from main_service
        message = "Successfully updated user"
    else: # nothing found so add new user
        await database.execute(insert_new_user(user))  #  No data was found, we need to insert new data
        message = "Successfully added a new user"

    return message


@app.get("/user")
async def get_user(user_id: str) -> User:
    results = await database.fetch_all(get_user_by_id_query(user_id))

    # since convert_data_to_module returns a list we just need to return index 0
    return convert_data_to_module(results)[0]


@app.get("/user/all")
async def get_all_users():
    results = await database.fetch_all(get_all_users_query())

    return convert_data_to_module(results)

