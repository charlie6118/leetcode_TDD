class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        min_str = strs[0]
        for idx in range(1, len(strs)):
            while min_str != strs[idx][:len(min_str)]:
                if len(min_str) == 0: return ""
                min_str = min_str[:-1]
                print(min_str)
        return min_str