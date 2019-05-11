import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49