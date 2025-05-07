from typing import Union

from fastapi import FastAPI

app = FastAPI(title="University API")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/status")
async def status():
    return {"message": "OK"}