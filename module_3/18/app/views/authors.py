from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.authors import AuthorSchema
from app.container import author_service


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

authors_ns = Namespace('authors')


@authors_ns.route('/')
class AuthorsView(Resource):

    def get(self):
        all_authors = author_service.get_all()
        return authors_schema.dump(all_authors), 200

    def post(self):
        req_json = request.get_json()
        author_service.create(req_json)

        return "", 201


@authors_ns.route('/<int:aid>')
class AuthorView(Resource):

    def get(self, aid: int):
        try:
            author = author_service.get_one(aid)
            return author_schema.dump(author), 200
        except Exception as e:
            return str(e), 404

    def put(self, aid: int):
        req_json = request.get_json()
        req_json["id"] = aid
        author_service.update(req_json)

        return "", 200

    def patch(self, aid: int):
        req_json = request.get_json()
        author_service.update_partial(req_json)

        return "", 204

    def delete(self, aid: int):
        author_service.delete(aid)

        return "", 204
