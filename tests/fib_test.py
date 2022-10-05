import pytest

from math_series.math_series import Fibonacci

def test_zero_ele():
    actual = Fibonacci(0)
    expected = 0
    assert actual == expected

def test_one_ele():
    actual = Fibonacci(1)
    expected = 1
    assert actual == expected

def test_two_ele():
    actual = Fibonacci(2)
    expected = 1
    assert actual == expected

def test_five_ele():
    actual = Fibonacci(5)
    expected = 5
    assert actual == expected

def test_six_ele():
    actual = Fibonacci(6)
    expected = 8
    assert actual == expected

def test_not_a_number():
    actual = Fibonacci("HELLO")
    expected = "IT'S NOT A NUMBER"
    assert actual == expected
