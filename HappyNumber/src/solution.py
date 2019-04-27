class Solution(object):
    def compute(self, n):
        sum = 0
        while n % 10 != 0:
            sum += (n % 10) ** 2
            n = n // 10
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in dp:
                return False
            else:
                dp.add(n)
        return True