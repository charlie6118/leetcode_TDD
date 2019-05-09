class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        max_substr = ""
        for i in range(len(s) + 1):
            for j in range(len(s) + 1):
                sub_str = s[i:j]
                if sub_str in dic:
                    continue
                dic[sub_str] = 1
                if len(sub_str) % 2 == 0:
                    if sub_str[0:len(sub_str) // 2] == sub_str[len(sub_str) // 2:len(sub_str)][::-1]:
                        if len(sub_str) > len(max_substr):
                            max_substr = sub_str
                if len(sub_str) % 2 != 0:
                    if sub_str[0: (len(sub_str) - 1) // 2] == sub_str[(len(sub_str) - 1) // 2 + 1: len(sub_str)][::-1]:
                        if len(sub_str) > len(max_substr):
                            max_substr = sub_str
        return max_substr