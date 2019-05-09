class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > n:
                return num