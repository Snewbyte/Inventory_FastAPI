from pydantic import BaseModel


class User(BaseModel):
    ID: int
    FirstName: str
    LastName: str
    Age: str
    Country: str
