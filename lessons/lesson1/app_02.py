from fastapi import FastAPI
import logging
from fastapi.responses import HTMLResponse, JSONResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"

@app.get("/message")
async def read_message():
    message = {"message":"Hello World"}
    return JSONResponse(content=message, status_code=200)


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/users/{user_id}/orders/{order_id}")
async def read_data(user_id: int, order_id: int):
    return {"user_id": user_id, "order_id": order_id}
