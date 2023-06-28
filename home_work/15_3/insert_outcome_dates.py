import sqlite3


with sqlite3.connect("animal.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT outcome_month, outcome_year
    FROM animals
    """)
    data_outcome_dates = cur.fetchall()

    insert_to_outcome_dates = """
    INSERT INTO outcome_dates (outcome_month, outcome_year)
    VALUES (?, ?)
    """
    cur.executemany(insert_to_outcome_dates, data_outcome_dates)
