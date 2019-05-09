class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2: return s
        table = []
        for _ in range(numRows):
            table.append([])
        cnt_up = True
        row_cnt_up = 0
        cnt_down = False
        row_cnt_down = numRows - 2
        for c in s:
            print(c)
            if cnt_up:
                table[row_cnt_up].append(c)
                row_cnt_up += 1
                if row_cnt_up > numRows - 1:
                    row_cnt_up = 0
                    cnt_up = False
                    cnt_down = True
                    # if only two rows, keep use cnt_up
                    if numRows == 2:
                        cnt_up = True
                        cnt_down = False
            elif cnt_down:
                table[row_cnt_down].append(c)
                row_cnt_down -= 1
                if row_cnt_down <= 0:
                    row_cnt_down = numRows - 2
                    cnt_down = False
                    cnt_up = True
            print(table)
        result = ""
        for row in table:
            for col in row:
                result += col
        return result