import pytest
from utils2 import get_verbal_grade

grade_parameters = [
    (2, "Погано"),
    (3, "Задовільно"),
    (4, "Добре"),
    (5, "Відмінно"),
]


@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_get_verbal_grade(grade_int, grade_str):
    assert get_verbal_grade(grade_int) == grade_str


grade_exceptions = [
    (1, ValueError),
    (6, ValueError),
    ('5', TypeError),
    (3.5, TypeError)
]


@pytest.mark.parametrize("grade_int, exceptions", grade_exceptions)
def test_get_verbal_exceptions(grade_int, exceptions):
    with pytest.raises(exceptions):
        assert get_verbal_grade(grade_int)


