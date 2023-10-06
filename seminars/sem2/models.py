from pydantic import BaseModel, Field
from datetime import date


class UserIn(BaseModel):
    name: str = Field(..., min_length=2)
    surname: str = Field(..., min_length=2)
    birthday: date = Field(..., format="%Y-%m-%d")
    adress: str = Field(..., )
    email: str = Field(..., max_length=128)
    password: str = Field(..., min_length=6)


class User(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)
