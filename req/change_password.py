import bcrypt
from pydantic import BaseModel

from .app import app
from models import User


class UserChangePassword(BaseModel):
    token: str
    new_password: str


@app.post("/change_password")
async def change_password(request: UserChangePassword):

    user = await User.query.where(User.token == request.token).gino.first()

    if user is None:
        return {"success": False}

    await user.update(
        password_hash=bcrypt.hashpw(
            request.new_password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
    ).apply()

    return {"success": True}
