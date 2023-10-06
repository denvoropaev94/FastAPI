from datetime import datetime
import databases
from settings import settings
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
    sqlalchemy.Column("birthday", sqlalchemy.Date),
    sqlalchemy.Column("adreses", sqlalchemy.String(128)),
    sqlalchemy.Column("surname", sqlalchemy.String(128)),
)

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("price", sqlalchemy.Float(128)),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("product_id", sqlalchemy.Integer, ForeignKey("products.id"), nullable=False),
    sqlalchemy.Column("date_order", sqlalchemy.String(64), nullable=False,
                      default=datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
                      onupdate=datetime.now().strftime("%d/%m/%y, %H:%M:%S")),
    sqlalchemy.Column("status", sqlalchemy.String(32))
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
