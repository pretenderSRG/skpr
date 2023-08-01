from flask import request
from flask_restx import Resource, Namespace
from app.models.books import BookSchema, Book

from app.database import db


books_ns = Namespace('books')
book_schema = BookSchema()
books_schema = BookSchema(many=True)


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

