import datetime

from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str = Field(..., min_length=2)
    surname: str = Field(..., min_length=2)
    birthday: datetime.date = Field(..., format="%Y-%m-%d")
    adreses: str = Field(..., )
    email: str = Field(..., max_length=128)
    password: str = Field(..., min_length=6)


class User(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)


class ProductIn(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)


class Product(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)


class OrderIn(BaseModel):
    status: str


class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    date_order: str
    status: str
