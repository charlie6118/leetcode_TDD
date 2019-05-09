import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.isHappy(19) == True

def test_case_compute():
    assert s.compute(19) == 82

def test_case1():
    assert s.isHappy(200) == False

def test_case2():
    assert s.isHappy(100) == True