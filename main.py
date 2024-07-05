import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from typing import List

from func import get_organizations


app = FastAPI(title="miac_anketa_api")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    # Возвращаем HTML-файл из статической папки
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.on_event("startup")
async def startup_event():
    pass
    # await db.set_bind(settings.pg_url)
    # await db.gino.create_all()
    # await insert_messages(settings.file_path)


@app.get("/organizations", response_model=List[list])
async def read_emails():
    return get_organizations()


if __name__ == "__main__":
    uvicorn_process = uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8021,
        reload=True,
        workers=2,
    )
