from app.dao.models.books import Book


class BookDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Book).all()

    def get_one(self, bid):
         return self.session.query(Book).filter(Book.id == bid).one()

    def create(self, data):
        book = Book(**data)

        self.session.add(book)
        self.session.commit()

        return book

    def update(self, book):
        self.session.add(book)
        self.session.commit()

        return book

    def delete(self, bid):
        book = self.get_one(bid)
        self.session.delete(book)
        self.session.commit()