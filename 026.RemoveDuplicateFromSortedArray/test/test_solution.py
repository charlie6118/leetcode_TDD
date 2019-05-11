import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.removeDuplicates([1, 1, 2]) == 2

def test_case1():
    assert s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5