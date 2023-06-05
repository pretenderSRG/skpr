import pytest
from movie_dao import MovieDAO


@pytest.fixture()
def movie_dao():
    return MovieDAO()


@pytest.fixture()
def correct_keys():
    return {"title", "trailer", "year", "rating", "pk"}
