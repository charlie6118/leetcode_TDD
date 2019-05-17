import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.strStr("abc", "") == 0
    assert s.strStr("misisipi", "pi") == 6