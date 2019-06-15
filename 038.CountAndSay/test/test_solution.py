import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.countAndSay(0) == "n should in range 1 ~ 30"
    assert s.countAndSay(1) == "1"
    assert s.countAndSay(2) == "11"
    assert s.countAndSay(3) == "21"
    assert s.countAndSay(4) == "1211"
    assert s.countAndSay(5) == "111221"
    assert s.countAndSay(6) == "312211"
    assert s.countAndSay(7) == "13112221"