from flask import request
from flask_restx import Resource, Namespace
from app.models import AuthorSchema, Author
from app.database import db
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)


authors_ns = Namespace('authors')


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
