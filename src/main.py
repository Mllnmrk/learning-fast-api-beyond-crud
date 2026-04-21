from fastapi import FastAPI

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/parameter/{sample}")
async def parameter(sample: str):
    return {"sample": f"this is the parameter: {sample}"}


@app.get("/query-parameter")
async def query_parameter(name: str) -> dict:
    return {"name": f"this is the query parameter: {name}"}
