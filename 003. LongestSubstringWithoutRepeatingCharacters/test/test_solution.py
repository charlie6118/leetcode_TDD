import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.lengthOfLongestSubstring("abcabcbb") == 3

def test_case1():
    assert s.lengthOfLongestSubstring("bbbbb") == 1

def test_case2():
    assert s.lengthOfLongestSubstring("pwwkew") == 3

def test_case3():
    assert s.lengthOfLongestSubstring("au") == 2

def test_case4():
    assert s.lengthOfLongestSubstring("dvdf") == 3

def test_case_emptyStr():
    assert s.lengthOfLongestSubstring("") == 0

def test_case_oneChar():
    assert s.lengthOfLongestSubstring("A") == 1