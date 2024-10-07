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
async def read_login():
    with open("templates/Login.html") as file:
        return HTMLResponse(content=file.read())

@app.get("/admin", response_class=HTMLResponse)
async def read_admin_page():
    with open("templates/Adminpage.html") as file:
        return HTMLResponse(content=file.read())

@app.get("/home", response_class=HTMLResponse)
async def read_homepage():
    with open("templates/homepage.html") as file:
        return HTMLResponse(content=file.read())

@app.get("/searchroom", response_class=HTMLResponse)
async def read_searchroom():
    with open("templates/search_room.html") as file:
        return HTMLResponse(content=file.read())
