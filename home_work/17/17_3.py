import os

from flask import Flask, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'movie.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSON_AS_ASCII"] = False

db = SQLAlchemy(app)


#  Movie models
class Movie(db.Model):
    __tablename__ = "movie"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    trailer = db.Column(db.Text)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, ForeignKey("director.id"))


# Genre models
class Genre(db.Model):
    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# Director models
class Director(db.Model):
    __tablename__ = "director"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# Movie Schema
class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()


# Genre Schema
class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


# Director Schema
class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


# create schemas exemplars
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

# create Api and name spaces
api = Api(app)
movie_ns = api.namespace('movies')
genre_ns = api.namespace('genres')
director_ns = api.namespace('directors')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        movie_list = []

        if director_id and genre_id:
            movies = db.session.query(Movie).filter(Movie.director_id == director_id, Movie.genre_id == genre_id)
            for movie in movies:
                movie_list.append(movie)
            if len(movie_list) == 0:
                return "Movies not found", 404
            return movies_schema.dump(movie_list), 200

        elif director_id:
            movies_by_director = db.session.query(Movie).filter(Movie.director_id == director_id)
            for movie in movies_by_director:
                movie_list.append(movie)
            if len(movie_list) == 0:
                return "Movies by director not found", 404
            return movies_schema.dump(movie_list), 200

        elif genre_id:
            movies_by_genre = db.session.query(Movie).filter(Movie.genre_id == genre_id)
            for movie in movies_by_genre:
                movie_list.append(movie)
            if len(movie_list) == 0:
                return "Movies by genre not found", 404
            return movies_schema.dump(movie_list), 200

        all_movies = db.session.query(Movie).all()
        return movies_schema.dump(all_movies), 200


    def post(self):
        rq_json = request.get_json()
        new_movie = Movie(**rq_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        try:
            movie = db.session.query(Movie).filter(Movie.id == mid).one()
            return movie_schema.dump(movie), 200
        except Exception as e:
            return f"Error --Movie not found--", 404

    def put(self, mid):
        rq_json = request.get_json()
        movie = db.session.query(Movie).get(mid)

        movie.title = rq_json.get("title")
        movie.description = rq_json.get("description")
        movie.trailer = rq_json.get("trailer")
        movie.year = rq_json.get("year")
        movie.rating = rq_json.get("rating")
        movie.genre_id = rq_json.get("genre_id")
        movie.director_id = rq_json.get("director_id")

        db.session.add(movie)
        db.session.commit()
        return "", 201

    def patch(self, mid):
        rq_json = request.get_json()
        movie = db.session.query(Movie).get(mid)

        if "title" in rq_json:
            movie.title = rq_json.get("title")
        if "description" in rq_json:
            movie.description = rq_json.get("description")
        if "trailer" in rq_json:
            movie.trailer = rq_json.get("trailer")
        if "year" in rq_json:
            movie.year = rq_json.get("year")
        if "rating" in rq_json:
            movie.rating = rq_json.get("rating")
        if "genre_id" in rq_json:
            movie.genre_id = rq_json.get("genre_id")
        if "director_id" in rq_json:
            movie.director_id = rq_json.get("director_id")

        db.session.add(movie)
        db.session.commit()

        return "", 201

    def delete(self, mid):
        movie = db.session.query(Movie).get(mid)
        db.session.delete(movie)
        db.session.commit()
        return "", 204


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = db.session.query(Director).all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        sq_json = request.get_json()
        new_director = Director(**sq_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        try:
            director = db.session.query(Director).filter(Director.id == did).one()
            return director_schema.dump(director)
        except Exception as e:
            return "Director not found", 404

    def put(self, did):
        rq_json = request.get_json()
        director = db.session.query(Director).get(did)

        director.name = rq_json.get("name")
        db.session.add(director)
        db.session.commit()
        return "", 201

    def patch(self, did):
        rq_json = request.get_json()
        director = db.session.query(Director).get(did)

        if "name" in rq_json:
            director.name = rq_json.get("name")
        db.session.add(director)
        db.session.commit()

        return "", 201

    def delete(self, did):
        director = db.session.query(Director).get(did)
        db.session.delete(director)
        db.session.commit()
        return "", 204


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = db.session.query(Genre).all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        sq_json = request.get_json()
        new_genre = Genre(**sq_json)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        try:
            genre = db.session.query(Genre).filter(Genre.id == gid).one()
            return genre_schema.dump(genre)
        except Exception as e:
            return "Director not found", 404

    def put(self, gid):
        rq_json = request.get_json()
        genre = db.session.query(Genre).get(gid)

        genre.name = rq_json.get("name")
        db.session.add(genre)
        db.session.commit()
        return "", 201

    def patch(self, gid):
        rq_json = request.get_json()
        genre = db.session.query(Genre).get(gid)

        if "name" in rq_json:
            genre.name = rq_json.get("name")
        db.session.add(genre)
        db.session.commit()

        return "", 201

    def delete(self, gid):
        genre = db.session.query(Director).get(gid)
        db.session.delete(genre)
        db.session.commit()
        return "", 204


if __name__ == '__main__':
    app.run(debug=True)
