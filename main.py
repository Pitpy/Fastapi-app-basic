from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import file, user
from fastapi.staticfiles import StaticFiles
import os
from fastapi.responses import FileResponse

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

# Create static directory if it doesn't exist
static_dir = os.path.join(os.path.dirname(__file__), "pages")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

# Mount the static directory
app.mount("/pages", StaticFiles(directory=static_dir), name="pages")

@app.get("/page")
async def get_html():
    html_file_path = os.path.join(static_dir, 'index.html')
    if os.path.isfile(html_file_path):
        return FileResponse(html_file_path)
    return {"error": "File not found"}

app.include_router(user.router)
app.include_router(file.router)