from fastapi import FastAPI

from routes.book import router as book_router

app = FastAPI(docs_url=None, redoc_url=None)

app.include_router(book_router)
