import pytest
from utils import has_r


def test_has_r():
    assert has_r("world") is True, "has R"
    assert has_r("wood") is False, "do'nt has R"
