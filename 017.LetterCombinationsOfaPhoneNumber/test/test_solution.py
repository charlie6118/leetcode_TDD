import pytest
from src.solution import Solution

s = Solution()

def test_len0():
    assert s.letterCombinations("") == []

def test_len1():
    assert s.letterCombinations("2") == "abc"

def test_case0():
    assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

def test_case1():
    assert s.letterCombinations("234") == ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]