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
                name nvarchar(40) NOT NULL,
                author nvarchar(40),
                description nvarchar(255),
                genre nvarchar(20) CONSTRAINT df_genre DEFAULT 'Undefined',
                publication_date date,
                pages_count integer CONSTRAINT ck_pages_count CHECK (pages_count > 0),
                price decimal                
                )    
                """
        # cursor.execute(query)

        index_query = f"""
                        CREATE INDEX book_name_idx ON {name} (name) 
                        """
        cursor.execute(index_query)
# create_bd()


create_table("Tarzan")
