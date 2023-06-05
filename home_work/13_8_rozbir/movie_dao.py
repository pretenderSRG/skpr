import json


class MovieDAO:

    def __init__(self):
        pass

    def load_data(self):
        with open("data.json", 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_by_id(self, movie_id):
        movies = self.load_data()

        for movie in movies:
            if movie.get("pk") == movie_id:
                return movie
        return None

    def get_by_period(self, movie_from, movie_to):
        movies = self.load_data()
        return [movie for movie in movies if movie_from <= movie.get("year") <= movie_to]

