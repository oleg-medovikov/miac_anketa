from .app import app
from typing import List

from models import User, Log


@app.get("/get_logs", response_model=List[dict])
async def get_logs():
    logs = (
        await Log.join(User, Log.user_id == User.guid)
        .select()
        .order_by(Log.time.desc())
        .limit(30)
        .gino.all()
    )
    return [
        {
            "time": log.time.strftime("%Y-%m-%d %H:%M:%S"),
            "username": log.fio,
            "event": log.event,
        }
        for log in logs
    ]
