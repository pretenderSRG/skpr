import sqlite3


with sqlite3.connect("animal.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT "animal_id",
            "animal_type",
            "name",
             "breed",
             "date_of_birth"
    FROM animals
    """)
    data_animals_1 = cur.fetchall()

    insert_to_animals_1 = """
    INSERT INTO animals_1 VALUES (?, ?, ?, ?, ?)
    """
    cur.executemany(insert_to_animals_1, data_animals_1)
