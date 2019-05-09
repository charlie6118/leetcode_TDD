import pytest
from src.solution import Solution

s = Solution()

def test_extendFromMiddle():
    assert s.extendFromMiddle("babad", 2, 2) == "aba" 

def test_case0():
    assert s.longestPalindrome("babad") == "bab"

def test_case1():
    assert s.longestPalindrome("cbbd") == "bb"