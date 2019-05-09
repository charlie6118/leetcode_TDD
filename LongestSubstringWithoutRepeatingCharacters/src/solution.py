class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # sliding window algorithm
        if len(s) < 2: return len(s)
        dic = {}
        max_len = 0
        start = 0
        for i, c in enumerate(s):
            if c in dic.keys() and start <= dic[c]:
                start = dic[c] + 1
            else:
                max_len = max(max_len, i - start + 1)
            dic[c] = i
        return max_len