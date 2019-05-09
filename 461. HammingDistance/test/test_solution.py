import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.hammingDistance(3, 1) == 1

def test_case1():
    assert s.hammingDistance(1, 4) == 2
