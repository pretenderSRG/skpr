class BookService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        bid = data.get("id")
        book = self.get_one(bid)

        book.name = data.get('name')
        book.author = data.get('author')
        book.year = data.get('year')

        self.dao.update(book)

    def update_partial(self, data):
        bid = data.get("id")
        book = self.get_one(bid)

        if 'name' in data:
            book.name = data.get('name')
        if 'author' in data:
            book.author = data.get('author')
        if 'year' in data:
            book.year = data.get('year')

        self.dao.update(book)

    def delete(self, aid):
        self.dao.delete(aid)

