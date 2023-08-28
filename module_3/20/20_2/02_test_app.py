import pytest
from unittest.mock import MagicMock


#  app.py
class ProductionClass:
    def m1(self):
        print("print m1")

    def m2(self):
        print("print m2")


# test_app.py
@pytest.fixture()
def prod_class():
    pc = ProductionClass()
    pc.m1 = MagicMock(return_value="123")
    pc.m2 = MagicMock(return_value="321")
    return pc


def test_pc(prod_class):
    assert prod_class.m1() == "123"
    assert prod_class.m2() == "321"
