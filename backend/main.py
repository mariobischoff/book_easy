from typing import Union

from fastapi import FastAPI
from routers import services

app = FastAPI()

app.include_router(services.router, prefix="/services")

@app.get("/")
def read_root():
    return {"Hello": "World"}
