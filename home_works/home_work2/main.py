import uvicorn
from fastapi import FastAPI

import orders
import products
import users
from db import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users.user_router, tags=["users"])
app.include_router(products.product_router, tags=["products"])
app.include_router(orders.order_router, tags=["orders"])

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
