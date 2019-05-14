import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(1121) == False
    assert s.isPalindrome(-121) == False
    assert s.isPalindrome(10) == False