from fastapi.responses import FileResponse
from pydantic import BaseModel

from .app import app
from func import create_anketa


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
