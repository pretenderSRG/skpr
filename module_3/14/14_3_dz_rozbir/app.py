from flask import Flask, jsonify, abort
import sqlite3


def main():
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False
    app.config["DEBUG"] = True

    def db_connect(query):
        with sqlite3.connect("netflix.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    @app.route('/movie/<title>')
    def search_by_title(title):
        query = f"""
        SELECT 
            title,
            country,
            release_year,
            listed_in as genre,
            description
        FROM netflix
        WHERE title = '{title}'
        ORDER by release_year DESC
        LIMIT 1
                """
        response_json = {}
        try:
            response = db_connect(query)[0]
            response_json = {
                "title": response[0],
                "country": response[1],
                "release_year": response[2],
                "genre": response[3],
                "description": response[4].strip(),
            }
        except IndexError:
            abort(404)
        return jsonify(response_json)

    @app.route('/movie/<int:start>/to/<int:end>')
    def search_by_years(start, end):
        query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {start} ANd {end}
        ORDER BY release_year
        LIMIT 100
        """
        
        response_json = []
        try:
            response = db_connect(query)
            for film in response:
                response_json.append({
                    "title": film[0],
                    "release_year": film[1]
                })
        except IndexError:
            response_json = []
        return jsonify(response_json)

    @app.route('/rating/<group>')
    def search_by_rating(group):
        levels = {
            'children': ['G'],
            'family': ['G', 'PG', 'PG-13'],
            'adult': ['R', 'NC-17'],
        }
        if group.lower() in levels:
            level = '\", \"'.join(levels[group])
            level = f'\"{level}\"'
        else:
            return jsonify([])
        query = f"""
                SELECT title,
                        rating,
                        description
                FROM netflix
                WHERE rating in ({level})
                """
        response = db_connect(query)
        response_json = []
        for film in response:
            response_json.append({
                "title": film[0],
                "rating": film[1],
                "description": film[2].strip()
            })
        return jsonify(response_json)

    @app.route('/genre/<genre>')
    def search_by_genre(genre):
        query = f"""
                SELECT title, description, listed_in
                FROM netflix
                WHERE listed_in LIKE "%{genre.title()}%"
                ORDER BY release_year DESC
                LIMIT 10
                """
        response = db_connect(query)
        response_json = []
        for film in response:
            response_json.append({
                "title": film[0],
                "listed_in": film[2],
                "description": film[1].strip(),
            })
        return jsonify(response_json)

    @app.errorhandler(404)
    def page_not_found(error):
        return "Page not found!!!!!!!!!", 404

    def get_actors(name1, name2):
        query = f"""
                SELECT "cast"
                FROM "netflix"
                WHERE "cast" LIKE '%{name1}%'
                AND "cast" LIKE '%{name2}%'
                """
        response = db_connect(query)
        actors = []
        for cast in response:
            actors.extend(cast[0].split(', '))
        result = []
        for actor in actors:
            if actor not in (name1, name2):
                if actors.count(actor) > 2:
                    result.append(actor)
        result = set(result)
        print(result)

    def get_films(film_type, year, genre):
        query = f"""
                SELECT title, description
                FROM netflix
                WHERE type = "{film_type}"
                AND release_year = {year}
                AND listed_in LIKE "%{genre}%"
                """
        result = db_connect(query)
        result_list = []
        for film in result:
            result_list.append({
                "title": film[0],
                "description": film[1].srip()
            })
        return result_list
    
   # get_actors("Rose McIver", "Ben Lamb")
    print(*get_films("Movie", 2020, "Action"), sep='\n')
    # app.run()

if __name__ == '__main__':
    main()
