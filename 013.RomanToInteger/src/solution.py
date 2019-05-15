class Solution(object):
    def mapRomanToInt(self, c):
        mapRomanToInt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if c in mapRomanToInt.keys():
            return mapRomanToInt[c]
        else:
            raise KeyError("There is no match Roman letter")
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for idx in range(len(s) - 1):
            if self.mapRomanToInt(s[idx]) < self.mapRomanToInt(s[idx + 1]):
                sum -= self.mapRomanToInt(s[idx])
            else:
                sum += self.mapRomanToInt(s[idx])
        sum += self.mapRomanToInt(s[-1])
        return sum