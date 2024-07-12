from fastapi import Request

from .app import app
from models import User


@app.get("/user_logout")
async def user_logout(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return False

    await User.update.values(token=None).where(User.token == auth_header).gino.status()
    return True
