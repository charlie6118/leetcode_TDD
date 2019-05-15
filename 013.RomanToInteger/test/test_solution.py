import pytest
from src.solution import Solution

s = Solution()

def test_case_map_roman_to_int():
    assert s.mapRomanToInt("I") == 1
    assert s.mapRomanToInt("V") == 5
    assert s.mapRomanToInt("X") == 10
    assert s.mapRomanToInt("L") == 50
    assert s.mapRomanToInt("C") == 100
    assert s.mapRomanToInt("D") == 500
    assert s.mapRomanToInt("M") == 1000
    with pytest.raises(KeyError) as excinfo:
        s.mapRomanToInt("c")
    assert excinfo.type == KeyError
    assert "There is no match Roman letter" in str(excinfo.value)

def test_case_single_char():
    assert s.romanToInt("I") == 1
    assert s.romanToInt("V") == 5
    assert s.romanToInt("X") == 10
    assert s.romanToInt("L") == 50
    assert s.romanToInt("III") == 3
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    pass