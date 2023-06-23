INSERT INTO genre (name)
VALUES ("Horror"), ("Sci-Fi");

INSERT INTO author (name)
VALUES ("Author 1"), ("Author 2"), ("Author 3");

INSERT INTO books (name, genre_id)
VALUES ("Book 1", 1), ("Book 2", 2), ("Book 3",2);

INSERT INTO books_author (book_id, author_id)
VALUES (1, 1), (2, 1), (2, 3)