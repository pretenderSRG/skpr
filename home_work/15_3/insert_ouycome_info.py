import sqlite3


with sqlite3.connect("animal.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT outcome_subtype, outcome_type, age_upon_outcome
    FROM animals
    """)
    data_outcome_info = cur.fetchall()

    insert_to_outcome_info = """
    INSERT INTO outcome_info (outcome_subtype, outcome_type, age_upon_outcome)
    VALUES (?, ?, ?)
    """
    cur.executemany(insert_to_outcome_info, data_outcome_info)
