from flask import Flask, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# books_ns = api.namespace('')

class Book(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)


class BookSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    author = fields.Str()
    year = fields.Int()


book_schema = BookSchema()
books_schema = BookSchema(many=True)

api = Api(app)
books_ns = api.namespace('')

b1 = Book(name="Harry Potter", year=2000, author="Joan Routing")
b2 = Book(name="Le Comte de Monte-Cristo", year=1844, author="Alexandre Dumas")

with app.app_context():
    db.create_all()

with db.session.begin():
    db.session.add_all([b1, b2])


@books_ns.route('/books')
class BooksView(Resource):

    def get(self):
        all_books = db.session.query(Book).all()
        return books_schema.dump(all_books), 200

    def post(self):
        req_json = request.get_json()
        new_book = Book(**req_json)
        with db.session.begin():
            db.session.add(new_book)
        return "", 201


@books_ns.route('/books/<int:bid>')
class BookView(Resource):

    def get(self, bid):
        return books[bid], 200

    def delete(self, bid):
        del books[bid]
        return "", 204


if __name__ == "__main__":
    app.run(debug=True)