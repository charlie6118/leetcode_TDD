class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = str('{:b}'.format(x))
        y = str('{:b}'.format(y))
        if len(y) > len(x):
            x = '0' * (len(y) - len(x)) + x
        else: y = '0' * (len(x) - len(y)) + y
            
        cnt = 0
        for idx in range(len(y)):
            if x[idx] != y[idx]:
                cnt += 1
        return cnt

        # leedcode fast solution
        # cnt = 0
        # while x > 0 or y > 0:
        #     if x % 2 != y % 2:
        #         cnt += 1
        #     x = x // 2
        #     y = y // 2
        # return cnt
