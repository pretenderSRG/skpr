import pytest

from conftest import number_42


@pytest.mark.skip(reason="Future test")
def test_ok(number_42):
    assert number_42 == 42


@pytest.mark.xfail()
def test_fail(number_42):
    assert number_42 == 42
