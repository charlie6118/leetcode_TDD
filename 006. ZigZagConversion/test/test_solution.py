import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.convert("1234567890", 3) == "1592468037"

def test_2Dlist():
    t = []
    t.append([])
    t.append([])
    t.append([])
    t[1].append(2)
    t[1].append(3)
    t[1].append(1)
    print(t)
    print(t[1])
    assert t[1][0] == 2
    assert t[1][1] == 3
    assert t[1][2] == 1
    assert t[1] != t[2]

def test_case1():
    assert s.convert("1234567890", 4) == "1726835940"

def test_case2():
    assert s.convert("ABC", 1) == "ABC"

def test_case3():
    assert s.convert("ABCDEF", 2) == "ACEBDF"

def test_case4():
    assert s.convert("ABCD", 2) == "ACBD"