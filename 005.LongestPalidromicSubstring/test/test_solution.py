import pytest
from src.solution import Solution

s = Solution()

def test_subStr():
    s_even = [1, 2, 3, 4]
    print(len(s_even))
    s_odd = [1, 2, 3]
    assert s_even[0:len(s_even) // 2] == [1, 2]
    assert s_even[len(s_even) // 2:len(s_even)] == [3, 4]

    assert s_odd[0:(len(s_odd) - 1) // 2] == [1]
    assert s_odd[(len(s_odd) - 1) // 2 + 1:len(s_odd)] == [3]

def test_case0():
    assert s.longestPalindrome("babad") == "bab"


def test_case1():
    assert s.longestPalindrome("cbbd") == "bb"