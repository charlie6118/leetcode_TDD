class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sort = sorted(nums)
        h = 0
        n = t = len(nums)
        t -= 1
        while h < n and nums[h] == nums_sort[h]:
            h += 1
        while t > h and nums[t] == nums_sort[t]:
            t -= 1
        return t - h + 1