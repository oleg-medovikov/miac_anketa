import bcrypt
from pydantic import BaseModel

from .app import app
from models import User


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
