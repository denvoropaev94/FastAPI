import uvicorn
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Genre(BaseModel):
    id: int
    title: str


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: Genre


genre_1 = Genre(id=1, title='Comedy')
genre_2 = Genre(id=1, title='Action')

collection = [
    Movie(id=1, title='Movie 1', description='novinka', genre=genre_1),
    Movie(id=2, title='Movie 2', description='very interesting', genre=genre_2)
]


@app.get('/movies/', response_model=list[Movie])
def movies(genre_title: str = None):
    if genre_title is None:
        return collection
    else:
        return [movie for movie in collection if movie.genre.title == genre_title]


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
