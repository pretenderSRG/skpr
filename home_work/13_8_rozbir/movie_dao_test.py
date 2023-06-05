import pytest


class TestMovieDAO:

    def test_load_data_is_list(self, movie_dao):
        data = movie_dao.load_data()
        assert type(data) == list
        assert len(data) > 0

        movie = data[0]
        assert type(movie) == dict, "Item of data not dict"

    def test_by_id_correct_type(self, movie_dao):
        movie_1 = movie_dao.get_by_id(1)
        assert type(movie_1) == dict, "Item of data not dict"

    def test_by_id_correct_keys(self, movie_dao, correct_keys):
        movie_1 = movie_dao.get_by_id(1)
        assert set(movie_1.keys()) == correct_keys, "Items keys is nor correct"

    def test_by_id_not_exists(self, movie_dao):
        movie_1 = movie_dao.get_by_id(-1)
        assert movie_1 is None

    def test_get_by_period_returns_list(self, movie_dao):
        movies_in_period = movie_dao.get_by_period(0, 300)
        assert type(movies_in_period) == list

    def test_by_period_not_exist(self, movie_dao):
        movies_in_period = movie_dao.get_by_period(-2, -1)
        assert movies_in_period == []

    def test_get_by_period_exist(self, movie_dao):
        movies_in_period = movie_dao.get_by_period(2010, 2018)
        assert len(movies_in_period) == 2

    def test_get_by_period_all(self, movie_dao):
        all_movies = movie_dao.load_data()
        all_movies_in_period = movie_dao.get_by_period(0, 3000)
        assert all_movies == all_movies_in_period

    def test_get_by_period_keys_correct(self, movie_dao, correct_keys):
        movie_1 = movie_dao.get_by_period(2008, 2008)[0]
        movie_keys = set(movie_1.keys())
        assert movie_keys == correct_keys, "Incorrect keys"

    @pytest.mark.parametrize(
        "movie_id, movie_name",
        [(1, "Hulk"), (2, "Fantastic 4"), (3, "Iron man")]
    )
    def test_get_by_id_values(self, movie_dao, movie_id, movie_name):
        movie = movie_dao.get_by_id(movie_id)
        assert movie.get("title") == movie_name
