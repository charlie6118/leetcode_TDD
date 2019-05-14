class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        new_num = 0
        old_num = x
        while x > 0:
            tmp = x % 10
            new_num = 10 * new_num + tmp
            x = x // 10
        return new_num == old_num