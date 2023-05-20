import pytest
from utils import double, ticket_price, divide, get_circle_square


class TestTicketPrice:

    def test_0(self):
        assert ticket_price(0) == "FREE", "Error for 0"

    def test_1(self):
        assert ticket_price(1) == "FREE", "Error for 1"

    def test_7(self):
        assert ticket_price(7) == "100 $", "Error for 7"

    def test_18(self):
        assert ticket_price(18) == "200 $", "Error for 7"

    def test_25(self):
        assert ticket_price(28) == "300 $", "Error for 25"

    def test_60(self):
        assert ticket_price(60) == "FREE", "Error for 60"

    def test_minus_1(self):
        assert ticket_price(-1) == "ERROR", "Error for -1"


def test_double_2():
    assert double(2) == 4


def test_double_3():
    assert double(3) == 6


def test_double_minus_5():
    assert double(-5) == -10


def test_double_float():
    assert double(2.2) == 4.4


def test_positive_int():
    assert divide(100, 10) == 10.0


def test_negative_int():
    assert divide(-20, -5) == 4.0


def test_zero_to_int():
    assert divide(0, 2) == 0.0


def test_float():
    assert divide(2.2, 2) == 1.1


def test_type_mismatch():
    with pytest.raises(TypeError):
        divide(True, None)


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(100, 0)


double_parameters = [(0, 0), (1, 2), (10.0, 20.0), (-3, -6), (123456789, 246913578)]


@pytest.mark.parametrize(
    "test_input, expected", double_parameters
)
def test_double(test_input, expected):
    assert double(test_input) == expected


def test_get_circle_square_normal_0():
    square = get_circle_square(0)
    assert square == 0, "Error to 0"


def test_get_circle_square_normal_1():
    square = get_circle_square(1)
    assert round(square, 2) == 3.14, "Error to 1"


def test_get_circle_square_normal_3():
    square = get_circle_square(3)
    assert round(square, 2) == 28.27, "Error to 3"


def test_get_circle_square_value_error():
    with pytest.raises(ValueError):
        get_circle_square(-2)


def test_get_circle_square_type_error():
    with pytest.raises(TypeError):
        get_circle_square("2")
