from typing import Optional

from fastapi import FastAPI, Header, Request
from pydantic import BaseModel

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/parameter/{sample}")
async def parameter(sample: str):
    return {"sample": f"this is the parameter: {sample}"}


@app.get("/query-parameter")
async def query_parameter(name: str = "Username", age: Optional[int] = 0) -> dict:
    return {"name": f"this is the query parameter: {name}", "age": age}


class Book(BaseModel):
    title: str
    author: str


@app.post("/book")
async def create_book(book: Book) -> dict:
    return {"title": book.title, "author": book.author}


@app.get("/header")
async def header(request: Request) -> str | dict | None:
    # request_header = dict(request.headers)
    accept = request.headers.get("accept")
    return accept
