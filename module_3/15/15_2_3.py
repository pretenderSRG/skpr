import sqlite3


with sqlite3.connect("books.db") as connection:
    cur = connection.cursor()
    cur.executescript("""

INSERT INTO books_author (book_id, author_id)
VALUES (1, 1), (2, 1), (2, 3)

    """)
    connection.commit()
