from pydantic import BaseModel
from enum import Enum


#class ProductTypeEnum(str, Enum):
#   FRUIT = "Fruit"
#   VEGETABLE = "Vegetable"


class Product(BaseModel):
    ID: int
    Name: str
    Price: float
    Type: str

class ProductRequest(BaseModel):
    ID: int
    Name: str
    Price: float
    Type: str

class ResponseMessage(BaseModel):
    content: str