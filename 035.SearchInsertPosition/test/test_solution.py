import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.searchInsert([1,3,5,6], 2) == 1
    assert s.searchInsert([1,3,5,6], 7) == 4
    assert s.searchInsert([1,3,5,6], 5) == 2