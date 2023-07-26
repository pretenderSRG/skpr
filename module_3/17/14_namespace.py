from flask import Flask, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, ForeignKey("authors.id"))

    authors = relationship("Author")


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    book = relationship("Book")


class BookSchema(Schema):

    id = fields.Int()
    name = fields.Str()
    year = fields.Int()
    author_id = fields.Int()


class AuthorSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()


book_schema = BookSchema()
books_schema = BookSchema(many=True)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)


api = Api(app)
books_ns = api.namespace('books')
authors_ns = api.namespace('authors')

a1 = Author(first_name="Joan", last_name="Routing")
a2 = Author(first_name="Alexandre", last_name="Dumas")

b1 = Book(name="Harry Potter", year=2000, authors=a1)
b2 = Book(name="Le Comte de Monte-Cristo", year=1844, authors=a2)

with app.app_context():
    db.create_all()
    with db.session.begin():
        db.session.add_all([a1, a2])
        db.session.add_all([b1, b2])


@books_ns.route('/')
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


@books_ns.route('/<int:bid>')
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


@authors_ns.route('/')
class AuthorsView(Resource):

    def get(self):
        all_authors = db.session.query(Author).all()
        return authors_schema.dump(all_authors), 200

    def post(self):
        req_json = request.get_json()
        new_author = Author(**req_json)
        with db.session.begin():
            db.session.add(new_author)
        return "", 201


@authors_ns.route('/<int:aid>')
class AuthorView(Resource):

    def get(self, aid: int):
        try:
            author = db.session.query(Author).filter(Author.id == aid).one()
            return author_schema.dump(author), 200
        except Exception as e:
            return str(e), 404

    def put(self, aid: int):
        author = db.session.query(Author).get(aid)
        req_json = request.get_json()

        author.first_name = req_json.get('first_name')
        author.last_name = req_json.get('last_name')

        db.session.add(author)
        db.session.commit()
        return "", 204

    def patch(self, aid: int):
        author = db.session.query(Author).get(aid)
        req_json = request.get_json()
        if 'first_name' in req_json:
            author.first_name = req_json.get('first_name')
        if 'last_name' in req_json:
            author.last_name = req_json.get('last_name')

        db.session.add(author)
        db.session.commit()
        return "", 204

    def delete(self, aid: int):
        author = db.session.query(Book).get(aid)
        db.session.delete(author)
        db.session.commit()
        return "", 204


if __name__ == "__main__":
    app.run(debug=True)
