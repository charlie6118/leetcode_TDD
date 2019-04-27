import pytest
from src.solution import Solution

s = Solution()

def test_case():
    assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6