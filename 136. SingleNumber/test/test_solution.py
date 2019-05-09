import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.singleNumber([2,2,1]) == 1

def test_case1():
    assert s.singleNumber([4,1,2,1,2]) == 4
