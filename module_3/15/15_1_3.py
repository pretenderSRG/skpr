import sqlite3


def create_bd():
    with sqlite3.connect("books_db.sqlite") as connection:
        cursor = connection.cursor()
        query = """
                
                """
        cursor.execute(query)


def create_table(name):
    with sqlite3.connect("books_db.sqlite") as connection:
        cursor = connection.cursor()
        query = f"""
                CREATE TABLE {name} (
                id integer PRIMARY KEY AUTOINCREMENT,
                name nvarchar(40),
                author nvarchar(40),
                description nvarchar(255),
                genre nvarchar(20),
                publication_date date,
                pages_count integer,
                price decimal                
                )    
                """
        cursor.execute(query)
# create_bd()


create_table("Tarzan")
