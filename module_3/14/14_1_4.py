import sqlite3


with sqlite3.connect("cars_1.db") as connection:
    cursor = connection.cursor()
    sql_query = ("""
    SELECT "price", "model" FROM cars
    WHERE "model" LIKE "V%"
    ORDER BY "price" DESC
    """)
    cursor.execute(sql_query)
    # print(cursor.fetchone())
    for row in cursor.fetchall():
        print(row)