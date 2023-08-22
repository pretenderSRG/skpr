import pytest
from app import sum_func


param = [(1, 2, 3), (-2, -50, -52), (0, 0, 0), (20, -20, 0)]


@pytest.mark.parametrize('data', param)
def test_sum_func(data: list):
    assert data[0] + data[1] == data[2]
    

def test_sum_func_fail_type():
    with pytest.raises(TypeError):
        sum_func('a', 10)



