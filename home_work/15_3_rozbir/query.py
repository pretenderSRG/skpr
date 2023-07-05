import sqlite3


def connect_db(query):
    try:
        with sqlite3.connect('animal.db') as conn:
            cur = conn.cursor()
            cur.execute(query)
            result = cur.fetchall()
    except FileNotFoundError:
        result = []
    return result


def main():
    create_colors_tbl = """
    CREATE TABLE IF NOT EXISTS colors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        color VARCHAR(50)
    )
    """
    connect_db(create_colors_tbl)

    insert_to_colors = """
    INSERT INTO colors (color)
    SELECT DISTINCT * FROM (
        SELECT DISTINCT
         color1 AS color 
        FROM animals
        UNION ALL
        SELECT DISTINCT
            color2 AS color
        FROM animals
        )
    """
    # connect_db(insert_to_colors)

    create_outcome_tb = """
    CREATE TABLE IF NOT EXISTS outcome (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subtype VARCHAR(50),
        "type" VARCHAR(50),
        "month" INTEGER,
        "year" INTEGER
    )
    """
    connect_db(create_outcome_tb)
    
    insert_to_outcome = """
    INSERT INTO outcome (subtype, "type", "month", "year")
    SELECT DISTINCT
        animals.outcome_subtype,
        animals.outcome_type,
        animals.outcome_month,
        animals.outcome_year
    FROM animals
    """
    # connect_db(insert_to_outcome)

    create_animals_final_tb = """
    CREATE TABLE IF NOT EXISTS animals_final (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age_upon_outcome VARCHAR(50),
        animal_id VARCHAR(50),
        animal_type VARCHAR(50),
        "name" VARCHAR(50),
        breed VARCHAR(50),
        date_of_birth VARCHAR(50),
        outcome_id INTEGER,
        FOREIGN KEY (outcome_id) REFERENCES outcome(id)
    )
    """
    connect_db(create_animals_final_tb)

    insert_to_animals_final = """
    INSERT INTO animals_final (age_upon_outcome, animal_id, animal_type, "name", breed, date_of_birth, outcome_id)
    SELECT
        animals.age_upon_outcome, animals.animal_id, animals.animal_type, animals.name, animals.breed, animals.date_of_birth, outcome.id
    FROM animals
    JOIN outcome
        ON outcome.subtype = animals.outcome_subtype
        AND outcome."type" = animals.outcome_type
        AND outcome."month" = animals.outcome_month
        AND outcome."year" = animals.outcome_year
    """
    connect_db(insert_to_animals_final)

    create_animals_colors_tbl = """
           CREATE TABLE IF NOT EXISTS animals_colors (
           animal_id INTEGER,
           color_id INTEGER,
           FOREIGN KEY (animal_id) REFERENCES animals_final(id),
           FOREIGN KEY (color_id) REFERENCES colors(id)
           )
       """
    connect_db(create_animals_colors_tbl)

    insert_to_animals_colors = """
        INSERT INTO animals_colors (animal_id, color_id)
        SELECT DISTINCT 
            animals_final.id, colors.id 
        FROM animals
        JOIN colors 
            ON colors.color = animals.color1
        JOIN animals_final
            ON animals_final.animal_id = animals.animal_id
        UNION ALL
        SELECT DISTINCT animals_final.id, colors.id
        FROM animals
        JOIN colors ON colors.color = animals.color2
        JOIN animals_final 
            ON animals_final.animal_id = animals.animal_id 
        """
    connect_db(insert_to_animals_colors)


if __name__ == '__main__':
    main()
