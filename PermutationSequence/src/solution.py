import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        n_list = [i for i in range(1, n + 1)]
        result = ""
        # by observation of test code result, so I tried k -= 1
        # (3, 3) -> 231
        # (4, 8) -> 2314
        # (4, 9) -> 2341
        # (4, 10) -> 2413
        k -= 1 
        while n_list:
            all_pos = math.factorial(len(n_list))
            gap = all_pos // len(n_list)
            digi = n_list[(k // gap)]
            k %= gap
            result += str(digi)
            n_list.remove(digi)
        return result