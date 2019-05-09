import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
    
def test_case1():
    assert s.findAnagrams("abab", "ab") == [0, 1, 2]
    
def test_case2():
    assert s.findAnagrams("abababab", "aab") == [0, 2, 4]
