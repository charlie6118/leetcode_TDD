import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.getPermutation(3, 3) == "213"

def test_case1():
    assert s.getPermutation(4, 9) == "2314"