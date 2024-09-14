from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_homepage():
    with open("templates/homepage.html") as file:
        content = file.read()
    return HTMLResponse(content=content)

@app.get("/searchroom", response_class=HTMLResponse)
async def read_searchroom():
    with open("templates/searchroom.html") as file:
        content = file.read()
    return HTMLResponse(content=content)
