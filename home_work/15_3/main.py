import sqlite3


with sqlite3.connect('animal.db') as conn:
    cur = conn.cursor()
    query = """
    SELECT *
    FROM animals
    """
    cur.execute(query)
    print(cur.fetchall())