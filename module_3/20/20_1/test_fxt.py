from app import sum_func


class TestSumFunc:
    def test_sum_positive(self):
        c = sum_func(1, 1)
        assert c > 0
        assert c == 2

    def test_sum_positive_and_negative(self):
        c = sum_func(1, -1)
        assert c == 0

    def test_sum_negative2(self):
        c = sum_func(-30, -10)
        assert c < 0
        assert c == -40
