from app.dao.models.authors import Author


class AuthorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Author).all()

    def get_one(self, aid):
        return self.session.query(Author).filter(Author.id == aid).one()

    def create(self, data):
        author = Author(**data)

        self.session.add(author)
        self.session.commit()

        return author

    def update(self, author):
        self.session.add(author)
        self.session.commit()

        return author

    def delete(self, aid):
        author = self.get_one(aid)

        self.session.delete(author)
        self.session.commit()
