from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from database import *

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

@app.get("/register", response_class=HTMLResponse)
async def get_register_page():
    with open("templates/sign_up.html") as file:
        return HTMLResponse(content=file.read())

@app.post("/register")
async def register_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    result = insert_new_person(username, email, password)
    if result:
        return RedirectResponse(url="/", status_code=303)
    return {"success": False, "message": "Registration failed."}

@app.get("/admin", response_class=HTMLResponse)
async def read_admin_page():
    with open("templates/dashboard.html") as file:
        return HTMLResponse(content=file.read())

@app.get("/home", response_class=HTMLResponse)
async def read_homepage():
    with open("templates/homepage.html") as file:
        return HTMLResponse(content=file.read())

@app.get("/searchroom", response_class=HTMLResponse)
async def read_searchroom():
    with open("templates/search_room.html") as file:
        return HTMLResponse(content=file.read())

@app.get("/room1", response_class=HTMLResponse)
async def read_room1():
    with open("templates/room_1.html") as file:
        return HTMLResponse(content=file.read())
    
@app.get("/room2", response_class=HTMLResponse)
async def read_room2():
    with open("templates/room_2.html") as file:
        return HTMLResponse(content=file.read())

@app.get("/room3", response_class=HTMLResponse)
async def read_room3():
    with open("templates/room_3.html") as file:
        return HTMLResponse(content=file.read())

@app.get("/room4", response_class=HTMLResponse)
async def read_room4():
    with open("templates/room_4.html") as file:
        return HTMLResponse(content=file.read())

@app.get("/room5", response_class=HTMLResponse)
async def read_room5():
    with open("templates/room_5.html") as file:
        return HTMLResponse(content=file.read())
