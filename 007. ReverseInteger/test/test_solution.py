import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.reverse(120) == 21

def test_case1():
    assert s.reverse(321) == 123

def test_case2():
    assert s.reverse(-321) == -123

def test_case3():
    assert s.reverse(1534236469) == 0


