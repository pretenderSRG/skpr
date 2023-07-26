from flask import Flask, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


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

    def get(self, bid: int):
        try:
            book = db.session.query(Book).filter(Book.id == bid).one()
            return book_schema.dump(book), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid: int):
        book = db.session.query(Book).get(bid)
        req_json = request.get_json()

        book.name = req_json.get('name')
        book.author = req_json.get('author')
        book.year = req_json.get('year')

        db.session.add(book)
        db.session.commit()
        return "", 204

    def patch(self, bid: int):
        book = db.session.query(Book).get(bid)
        req_json = request.get_json()
        if 'name' in req_json:
            book.name = req_json.get('name')
        if 'author' in req_json:
            book.author = req_json.get('author')
        if 'year' in req_json:
            book.year = req_json.get('year')

        db.session.add(book)
        db.session.commit()
        return "", 204

    def delete(self, bid: int):
        book = db.session.query(Book).get(bid)
        db.session.delete(book)
        db.session.commit()
        return "", 204


if __name__ == "__main__":
    app.run(debug=True)