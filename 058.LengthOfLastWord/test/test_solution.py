import pytest
from src.solution import Solution

s = Solution()

def test_case_edge():
    assert s.lengthOfLastWord("") == 0
    assert s.lengthOfLastWord(" ") == 0
    assert s.lengthOfLastWord("  ") == 0

def test_case():
    assert s.lengthOfLastWord("Hello World") == 5