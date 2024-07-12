from .base import db
from sqlalchemy.sql import func


class Log(db.Model):
    __tablename__ = "logs"

    time = db.Column(db.DateTime, primary_key=True, default=func.now())
    user_id = db.Column(db.SmallInteger, db.ForeignKey("users.guid"))
    event = db.Column(db.String(255), nullable=False)