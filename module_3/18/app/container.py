from app.dao.author import AuthorDAO
from app.dao.book import BookDAO
from app.services.author import AuthorService
from app.services.book import BookService
from app.database import db


author_dao = AuthorDAO(db.session)
author_service = AuthorService(author_dao)

book_dao = BookDAO(db.session)
book_service = BookService(book_dao)