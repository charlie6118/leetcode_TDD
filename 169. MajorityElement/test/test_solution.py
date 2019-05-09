import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.majorityElement([3, 2, 3]) == 3

