import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.smallestDiff([1, 5, 9, 20, 3]) == 2