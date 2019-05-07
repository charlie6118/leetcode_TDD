import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.maxProfit([1,2,3,0,2]) == 3