import sqlite3


class Car:
    def __init__(self, path_to_base):
        self.__path = path_to_base

    def __make_query(self, query):
        with sqlite3.connect(self.__path) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def find_by_model(self, model):
        query = f"""
        SELECT "model", "bodywork", MAX("year") as "max_year", "color", "description" 
        FROM "cars"
        WHERE "model" = '{model}'
        GROUP BY "model"
        """

        find_model = self.__make_query(query)

        return find_model[0]

    def find_range(self, start, stop):
        query = f"""
        SELECT "model", "year"
        FROM "cars"
        WHERE "year" BETWEEN {start} AND {stop}
        ORDER BY "year"
        """
        result = self.__make_query(query)
        return result




