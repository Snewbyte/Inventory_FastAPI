from pydantic import BaseModel
from enum import Enum


class ProductTypeEnum(str, Enum):
    FRUIT = "Fruit"
    VEGETABLE = "Vegetable"


class Product(BaseModel):
    ID: int
    Name: str
    Price: float
    Type: ProductTypeEnum

class ProductRequest(BaseModel):
    ID: int
    Name: str
    Price: float
    Type: ProductTypeEnum
