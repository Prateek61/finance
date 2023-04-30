from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db: SQLAlchemy = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Text, unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    date_time = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, category: str, amount: int, description: str, user_id: int):
        self.category = category
        self.amount = amount
        self.description = description
        self.user_id = user_id
        self.date_time = datetime.now().isoformat()