import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    # assert s.moveZeroes([0,1,0,3,12]) == [1, 3, 12, 0, 0]