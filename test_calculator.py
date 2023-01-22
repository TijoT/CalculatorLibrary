"""
Unit tests for calculator lib
"""

import Calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == Calculator.add(2, 3)

    def test_subtraction(self):
        assert 2 == Calculator.subtract(5, 3)
