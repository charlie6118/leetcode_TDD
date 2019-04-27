import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.maxProfit([7,1,5,3,6,4]) == 5