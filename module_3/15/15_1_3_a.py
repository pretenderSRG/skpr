import sqlite3


def modify_table():
    with sqlite3.connect("books_db.sqlite") as connection:
        cursor = connection.cursor()
        query = """
        ALTER TABLE Tarzan 
        ADD publication_country nvarchar(20)
        """

        query_delete_table = """
                            DROP TABLE Tarzan_3
                            """
        query_rename_table = """
                ALTER TABLE Tarzan 
                RENAME TO books
                """
        # cursor.execute(query)
        # cursor.execute(query_delete_table)
        cursor.execute(query_rename_table)


modify_table()