import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.rob([1, 2, 3, 1]) == 4

def test_case1():
    assert s.rob([2, 1, 1, 2]) == 4

def test_case2():
    assert s.rob([2, 1, 1, 100, 5, 1, 1]) == 103

def test_case3():
    assert s.rob([]) == 0