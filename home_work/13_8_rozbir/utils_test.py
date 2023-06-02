import pytest
from utils import has_r


def test_has_r_with():
    assert has_r("world") is True, "has R"


def test_has_r_without():
    pass


def test_has_r_wrong_type():
    pass