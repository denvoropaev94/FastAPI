import datetime

from fastapi import APIRouter
from db import database, orders, users, products
from models import Order, OrderIn

order_router = APIRouter()


@order_router.post("/order/{user_id}/{product_id}", response_model=OrderIn)
async def create_order(user_id: int, product_id: int, new_order: OrderIn):
    query = orders.insert().values(user_id=user_id, product_id=product_id,
                                   date_order=datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
                                   status=new_order.status)
    last_record_id = await database.execute(query)
    return {**new_order.dict(), "id": last_record_id}


@order_router.put("/order/{order_id}", response_model=OrderIn)
async def update_order(order_id, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(status=new_order.status)
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@order_router.get("/orders/")
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@order_router.get("/order/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@order_router.delete("/order/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)

    await database.execute(query)
    return {'message': 'Order deleted'}
