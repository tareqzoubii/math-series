from re import X
import pytest

from math_series.math_series import sum_series

def test_zero_ele_fibonacci():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_zero_ele_lucas():
    actual = sum_series(0,2,1)
    expected = 2
    assert actual == expected

def test_zero():
    actual = sum_series(0,2,2)
    expected = 2
    assert actual == expected

def test_one_ele_lucas():
    actual=sum_series(1,2,1)
    expected=1
    assert actual == expected

def test_one():
    actual=sum_series(1,8,9)
    expected=9
    assert actual == expected

def test_three_ele_fibonacci():
   actual=sum_series(3,0,1)
   expected=2
   assert actual == expected 

def test_three_ele_lucas():
    actual = sum_series(3,2,1)
    expected = 4
    assert actual == expected

def test_three():
    actual = sum_series(3,6,6)
    expected = 18
    assert actual == expected

def test_not_a_number():
    actual = sum_series("HELLO")
    expected = "IT'S NOT A NUMBER"
    assert actual == expected