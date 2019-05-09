class Solution(object):
    def extendFromMiddle(self,s, i, j):
        while  (i >= 0 and j < len(s)) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1: j]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        for i in range(len(s)):
            tmp = self.extendFromMiddle(s, i, i)
            if len(tmp) > len(r):
                r = tmp
            tmp = self.extendFromMiddle(s, i, i + 1)
            if len(tmp) > len(r):
                r = tmp
        return r

    def longestPalindrome_ultra(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s == s[::-1]:
                return s
        subHead, maxStrLen = 0, 1
        for idx in range(len(s)):
            odd = s[idx - maxStrLen - 1: idx + 1]
            even = s[idx - maxStrLen: idx + 1]    
            if idx-maxStrLen-1 >= 0 and odd == odd[::-1]:
                subHead = idx - maxStrLen - 1
                maxStrLen += 2
            elif idx - maxStrLen >= 0 and even == even[::-1]:
                subHead = idx - maxStrLen
                maxStrLen += 1  
        return s[subHead: subHead + maxStrLen]
