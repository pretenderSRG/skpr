import sqlite3


with sqlite3.connect("animal.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT color1, color2
    FROM animals
    """)
    data_colors = cur.fetchall()

    insert_to_color = """
    INSERT INTO colors (color1, color2)
    VALUES (?, ?)
    """
    cur.executemany(insert_to_color, data_colors)
