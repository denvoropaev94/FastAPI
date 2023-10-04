import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class UserAttrs(BaseModel):
    name: str
    email: str


class User(UserAttrs):
    id: int


collection = [
    User(id=1, name='Ivanov Ivan', email='ivan@ivanov.t'),
    User(id=2, name='Kuznecov Aleksey', email='aleksey@kuznecov.r')
]


@app.get('/users/', response_class=HTMLResponse)
def users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": collection})


@app.post('/users/')
def create_users(request: Request, name: Annotated[str, Form()], email: Annotated[str, Form()]):
    user = User(id=len(collection) + 1, email=email, name=name)
    collection.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "users": collection})


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
