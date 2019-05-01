import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.findUnsortedSubarray([2,6,4,8,10,9,15]) == 5

def test_case1():
    assert s.findUnsortedSubarray([1, 2, 3, 4]) == 0