from fastapi import Request

from .app import app
from models import User


@app.get("/check_token")
async def check_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return False

    user = await User.query.where(User.token == auth_header).gino.first()
    return {"token_valid": bool(user)}
