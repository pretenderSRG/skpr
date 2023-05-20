from math import pi


def double(value):
    """
    Make double of value
    :param value:
    :return: value * 2
    """
    new_value = value * 2
    return new_value


def ticket_price(age):
    """Make ticket price"""
    if 0 <= age < 7 or age >= 60:
        return "FREE"
    elif 7 <= age < 18:
        return "100 $"
    elif 18 <= age < 25:
        return "200 $"
    elif 25 <= age < 60:
        return "300 $"
    else:
        return "ERROR"


def divide(first, second):
    """
    Divides the first number by the second
    :param first:
    :param second:
    :return:
    """
    return first/second


def get_circle_square(radius):
    """
    Get square of circle
    :param radius:
    :return:
    """
    if type(radius) not in (int, float):
        raise TypeError("Radius must be int or float")

    if radius < 0:
        raise ValueError('Radius must be > 0')

    return radius ** 2 * pi
