import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]