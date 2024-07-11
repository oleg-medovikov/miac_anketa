import uvicorn
import bcrypt
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from contextlib import asynccontextmanager

from typing import List

from func import get_organizations, create_anketa, DB_URL
from models import db, User


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("execution before startup")
    await db.set_bind(DB_URL)
    await db.gino.create_all()
    yield print("Execute before closed")


app = FastAPI(title="miac_anketa_api", lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def get_main_page():
    # Читаем HTML-файл
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/login")
def get_login_page():
    # Читаем HTML-файл
    with open("static/login.html", "r") as f:
        html_content = f.read()

    return HTMLResponse(content=html_content, status_code=200)


@app.get("/organizations", response_model=List[list])
async def read_emails():
    return get_organizations()


class UserLoginRequest(BaseModel):
    username: str
    password: str


@app.post("/user_login")
async def user_login(request: UserLoginRequest):

    user = await User.query.where(User.username == request.username).gino.first()

    if user is None:
        return None

    if bcrypt.checkpw(
        request.password.encode("utf-8"), user.password_hash.encode("utf-8")
    ):
        token = await user.generate_token()
        return {"token": token}


@app.get("/check_token")
async def check_token(request: Request):
    auth_header = request.headers.get("Authorization")
    print(auth_header)
    if not auth_header:
        return False

    user = await User.query.where(User.token == auth_header).gino.first()
    return {"token_valid": bool(user)}


class OrganizationRequest(BaseModel):
    oid: str


@app.post("/get_excel")
async def get_excel(request: OrganizationRequest):
    file_path = create_anketa(request.oid)

    # Возвращаем файл для скачивания
    response = FileResponse(
        file_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="organization_report.xlsx",
    )
    return response


if __name__ == "__main__":
    uvicorn_process = uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8022,
        reload=True,
        workers=2,
    )
