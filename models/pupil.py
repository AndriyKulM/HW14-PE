from datetime import datetime
from email import message
from email.policy import default
from database import db


class PupilHomeTask(db.Model):
    __tablename__ = 'pupilhometasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(300), nullable=False, unique=True)
    home_tasks = db.Column(db.String(50), nullable=False)                 #  like a "submitted" or "not submitted"
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
