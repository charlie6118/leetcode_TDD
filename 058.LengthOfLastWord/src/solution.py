class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split()
        if arr and arr[-1]:
            return len(arr[-1])
        return 0