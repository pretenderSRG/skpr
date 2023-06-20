import sqlite3


def modify_table():
    with sqlite3.connect("books_db.sqlite") as connection:
        cursor = connection.cursor()
        query = """
        ALTER TABLE Tarzan RENAME description TO text
        """
        cursor.execute(query)


modify_table()