from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from databases import Database
import operator

from modules.user_module import User
from services.main_service import get_user_by_id_query, get_all_users_query, convert_data_to_module


class UserRequest(BaseModel):
    user_id: str
    last_name: str
    first_name: Union[str, None] = None


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
def modify_user(user: UserRequest):
    return f"New user {user.user_id}"


@app.get("/user")
async def get_user(user_id: str) -> User:
    results = await database.fetch_all(get_user_by_id_query(user_id))

    # since convert_data_to_module returns a list we just need to return index 0
    return convert_data_to_module(results)[0]


@app.get("/user/all")
async def get_all_users():
    results = await database.fetch_all(get_all_users_query())

    return convert_data_to_module(results)

