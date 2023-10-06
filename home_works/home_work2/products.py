from fastapi import APIRouter, HTTPException
from db import products, database
from typing import List
from models import Product, ProductIn

product_router = APIRouter()


# @router.get("/")
# async def home():
#     return {"Home_Work": "6"}


@product_router.get("/products/", response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@product_router.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(**product.dict())
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@product_router.get("/products/{product_id}", response_model=Product)
async def read_user(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@product_router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@product_router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'User deleted'}
