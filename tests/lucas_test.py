import pytest

from math_series.math_series import Lucas

def test_zero_ele():
    actual = Lucas(0)
    expected = 2
    assert actual == expected

def test_one_ele():
    actual = Lucas(1)
    expected = 1
    assert actual == expected

def test_two_ele():
    actual = Lucas(2)
    expected = 3
    assert actual == expected

def test_three_ele():
    actual = Lucas(3)
    expected = 4
    assert actual == expected

def test_five_ele():
    actual = Lucas(5)
    expected = 11
    assert actual == expected

def test_not_a_number():
    actual = Lucas("HELLO")
    expected = "IT'S NOT A NUMBER"
    assert actual == expected