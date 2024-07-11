from .base import db
from uuid import uuid4


class User(db.Model):
    __tablename__ = "users"

    guid = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    fio = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    token = db.Column(db.String(255), nullable=True)

    async def generate_token(self):
        token = str(uuid4())
        await self.update(token=token).apply()
        return token
