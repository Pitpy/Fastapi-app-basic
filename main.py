from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import file, user

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://localhost:3000",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.root_path = "/api/v1"

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

app.include_router(user.router)
app.include_router(file.router)