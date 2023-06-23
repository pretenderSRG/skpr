import sqlite3


def insert_to_table():
    with sqlite3.connect("books_db.sqlite") as connection:
        cursor = connection.cursor()
        query = """
                INSERT INTO books (name, author, description, genre, pages_count, price, publication_country)
                VALUES ("Tarzan", "Edgar Berrouse", "Story about monkey boy", "Fantasy", 324, 180, "USA")
            """

        query2 = """
                INSERT INTO books (name, author,pages_count)
                VALUES ("New book", "People", 200), ("New book 3", "Some one man", 100)
            """

        cursor.execute(query2)


# insert_to_table()

def update_table():
    with sqlite3.connect("books_db.sqlite") as connection:
        cursor = connection.cursor()
        query1 = """
                UPDATE books
                SET price = price + 0.3 * price
                WHERE id = 2
                
            """
        cursor.execute(query1)


update_table()