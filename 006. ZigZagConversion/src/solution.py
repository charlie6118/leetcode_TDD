class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2: 
            return s

        r = [""] * numRows
        step = 1
        pos = 0
        for c in s:
            r[pos] += c
            if pos == 0: 
                step = 1
            elif pos == numRows - 1:
                step = -1
            pos += step
        
        # return "".join(r)
        result = ""
        for row in r:
            for col in row:
                result += col
        return result