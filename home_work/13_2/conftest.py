import pytest


#  FIXTURES
@pytest.fixture
def positive_ang_negative_numbers():
    return [-1, 4]


@pytest.fixture
def positive_numbers():
    return [1, 1]


@pytest.fixture
def negative_numbers():
    return [-1, -1]
