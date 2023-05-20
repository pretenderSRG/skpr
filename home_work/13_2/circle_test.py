import pytest

from circle import Circle


class TestCircle:

    def test_get_radius(self):
        circle = Circle(1)
        assert circle.get_radius() == 1, "Помилка в радіусі"

    def test_get_diameter(self):
        circle = Circle(1)
        assert circle.get_diameter() == 2, "Помилка в діаметрі"

    def test_get_perimeter(self):
        circle = Circle(1)
        assert circle.get_perimeter() == 3.14, "Помилка в довжині кола"

    def test_init_type_error(self):
        with pytest.raises(TypeError):
            circle = Circle("1")

    def test_init_value_error(self):
        with pytest.raises(ValueError):
            circle = Circle(-1)
