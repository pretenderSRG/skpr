from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.dao.models.authors import Author
from app.dao.models.books import Book
from app.views.books import books_ns
from app.views.authors import authors_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(books_ns) # books
    api.add_namespace(authors_ns) # authors


def load_data():
    a1 = Author(first_name="Joan", last_name="Routing")
    a2 = Author(first_name="Alexandre", last_name="Dumas")

    b1 = Book(name="Harry Potter", year=2000, authors=a1)
    b2 = Book(name="Le Comte de Monte-Cristo", year=1844, authors=a2)

    with app.app_context():
        db.create_all()
        with db.session.begin():
            db.session.add_all([a1, a2])
            db.session.add_all([b1, b2])


if __name__ == "__main__":
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    load_data()

    app.run()
