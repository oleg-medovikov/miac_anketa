from fastapi.responses import FileResponse
from pydantic import BaseModel

from .app import app
from func import create_anketa
from models import User, Log


class OrganizationRequest(BaseModel):
    oid: str
    token: str


@app.post("/get_excel")
async def get_excel(request: OrganizationRequest):
    user = await User.query.where(User.token == request.token).gino.first()
    if not user:
        return None

    await Log.create(user_id=user.guid, event=f"Запрос анкеты для {request.oid}")

    file_path = create_anketa(request.oid)

    # Возвращаем файл для скачивания
    response = FileResponse(
        file_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="organization_report.xlsx",
    )
    return response
