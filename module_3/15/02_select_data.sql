SELECT books.name as book_name,
    genre.name as genre_name
FROM books
    INNER JOIN genre ON books.genre_id = genre.id