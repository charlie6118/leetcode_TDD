class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1 or n > 30: return "n should in range 1 ~ 30"
        
        re_str = "1"

        while n > 1:
            cnt = 0
            tmp = ""
            pre = re_str[0]
            for c in re_str:
                if pre == c:
                    cnt += 1
                else:
                    tmp = tmp + str(cnt) + pre
                    pre = c
                    cnt = 1
            tmp = tmp + str(cnt) + pre
            re_str = tmp
            n = n - 1

        return re_str