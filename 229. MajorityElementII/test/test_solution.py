import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.majorityElement([3, 2, 3]) == [3]

def test_case1():
    assert s.majorityElement([1,1,1,3,3,2,2,2]) == [1, 2]

def test_case3():
    assert s.majorityElement([1, 2]) == [1, 2]

def test_case4():
    assert s.majorityElement([0, 0, 0]) == [0]