import pytest
from main import app


def test_all():
    params = {"s": "python"}
    response = app.test_client().get("/", query_string=params)
    print(response.json)
    assert response.status_code == 200
    assert len(response.json) == 3


def test_one():
    params = {"s": "beginners"}
    response = app.test_client().get('/', query_string=params)
    print(response.json)
    assert response.status_code == 200
    assert len(response.json) == 1


def test_none():
    params = {"s" :"java"}
    response = app.test_client().get("/", query_string=params)
    print(response.json)
    assert response.status == 200
    assert len(response.json) == 0
