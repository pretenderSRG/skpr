import sqlite3


def search_by_id(id):
    with sqlite3.connect('animal.db') as con:
        cur = con.cursor()
        query = f"""
        SELECT *
        FROM animals_1
        INNER JOIN colors ON animals_1.color_id = colors.id
        WHERE "index" = {id}
        """
        cur.execute(query)
        result = cur.fetchone()
        return result