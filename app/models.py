from app import db
from sqlalchemy import Enum

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.Text, nullable=False)  # Store JSON as string
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(Enum("pending", "completed", name="order_status"), nullable=False, default="pending")
