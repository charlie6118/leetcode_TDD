import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.climbStairs(2) == 2

def test_case1():
    assert s.climbStairs(3) == 3