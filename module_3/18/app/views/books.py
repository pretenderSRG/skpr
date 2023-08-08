from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.books import BookSchema
from app.container import book_service


books_ns = Namespace('books')
book_schema = BookSchema()
books_schema = BookSchema(many=True)


@books_ns.route('/')
class BooksView(Resource):

    def get(self):
        all_books = book_service.get_all()
        return books_schema.dump(all_books), 200

    def post(self):
        req_json = request.get_json()
        book_service.create(req_json)

        return "", 201


@books_ns.route('/<int:bid>')
class BookView(Resource):

    def get(self, bid: int):
        try:
            book = book_service.get_one(bid)
            return book_schema.dump(book), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid: int):

        req_json = request.get_json()
        req_json["id"] = bid
        book_service.update(req_json)

        return "", 204

    def patch(self, bid: int):
        req_json = request.get_json()
        req_json["id"] = bid

        book_service.update_partial(req_json)
        
        return "", 204

    def delete(self, bid: int):
        book_service.delete(bid)
        return "", 204

