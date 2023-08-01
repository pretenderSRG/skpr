from app.database import db
from marshmallow import Schema, fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, ForeignKey("authors.id"))

    authors = relationship("Author")


class BookSchema(Schema):

    id = fields.Int()
    name = fields.Str()
    year = fields.Int()
    author_id = fields.Int()
