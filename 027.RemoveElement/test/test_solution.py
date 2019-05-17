import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.removeElement([3, 2, 2, 3], 3) == 2