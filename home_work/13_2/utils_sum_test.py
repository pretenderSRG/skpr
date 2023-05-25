import pytest

import conftest

from utils import sum_of_two


class TestSum:

    def test_sum_positive(self):
        c = sum_of_two(1, 1)
        assert c == 2

    def test_sum_positive_and_negative(self):
        c = sum_of_two(1, -1)
        assert c == 0

    def test_sum_ngative2(self):
        c = sum_of_two(-2, -1)
        assert c == -3


class TestSumFunc:

    def test_sum_positive(self, positive_numbers):
        c = sum_of_two(positive_numbers[0], positive_numbers[1])
        assert c > 0
        assert c == 2

    def test_sum_negative(self, negative_numbers):
        c = sum_of_two(negative_numbers[0], negative_numbers[1])
        assert c < 0
        assert c == -2

    def test_sum_positive_and_negative_numbers(self, positive_ang_negative_numbers):
        c = sum_of_two(positive_ang_negative_numbers[0], positive_ang_negative_numbers[1])
        assert c == 3
