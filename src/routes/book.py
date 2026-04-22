from typing import Optional

from fastapi import APIRouter, Request

from schemas.book import Book

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/parameter/{sample}")
async def parameter(sample: str):
    return {"sample": f"this is the parameter: {sample}"}


@router.get("/query-parameter")
async def query_parameter(name: str = "Username", age: Optional[int] = 0) -> dict:
    return {"name": f"this is the query parameter: {name}", "age": age}


@router.post("/book", status_code=201)
async def create_book(book: Book) -> dict:
    return {"title": book.title, "author": book.author}


@router.get("/header")
async def header(request: Request) -> str | dict | None:
    # request_header = dict(request.headers)
    accept = request.headers.get("accept")
    return accept
