from flask import Flask, abort, request

from flask_restx import Api, Resource


def login_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        return func(*args, **kwargs)
    return wrapper

app = Flask(__name__)
api = Api(app)
books_ns = api.namespace('')

@books_ns.route('/books')
class BooksView(Resource):
    def get(self):
        return "Work", 200

    @login_required
    def post(self):
        return '', 201


if __name__ == '__main__':
    app.run(debug=True)