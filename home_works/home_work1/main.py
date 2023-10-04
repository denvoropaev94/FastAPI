from fastapi import FastAPI, HTTPException
import uvicorn
from typing import Optional
from pydantic import BaseModel
from starlette.responses import HTMLResponse

app = FastAPI()


class UserParam(BaseModel):
    name: str
    surname: str
    email: str


class User(UserParam):
    id: int


users_collection = [
    User(id=1, name='Den', surname='Voropaev', email='denvorop@mail.ru'),
    User(id=2, name='Nik', surname='Bondarenko', email='bondar@mail.ru'),
    User(id=3, name='Oleg', surname='Belyavskiy', email='olega@mail.ru'),
]


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Home Work - FastAPI - Users</h1>"


@app.get('/users/', response_model=list[User])
def get_users():
    return users_collection


@app.get('/users/{id}', response_model=User)
def get_user(id: int):
    for user in users_collection:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post('/users/', response_model=User)
def create_user(params: UserParam):
    user = User(id=len(users_collection) + 1, **params.dict())
    users_collection.append(user)
    return user


@app.put('/tasks/{id}', response_model=User)
def update_task(id: int, params: UserParam):
    for user in users_collection:
        if user.id == id:
            user.name = params.name
            user.surname = params.surname
            user.email = params.email
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete('/user/{id}', response_model=dict)
def destroy_tasks(id: int):
    for user in users_collection:
        if user.id == id:
            users_collection.remove(user)
            return {'message': 'User deleted successfully'}
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
