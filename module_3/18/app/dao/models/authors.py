from app.database import db
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    book = relationship("Book")


class AuthorSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
