import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"

def test_case1():
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""