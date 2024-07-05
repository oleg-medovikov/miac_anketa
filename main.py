import uvicorn
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from typing import List

from func import get_organizations, create_anketa


app = FastAPI(title="miac_anketa_api")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    # Возвращаем HTML-файл из статической папки
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/organizations", response_model=List[list])
async def read_emails():
    return get_organizations()


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
