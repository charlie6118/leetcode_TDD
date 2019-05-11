class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                cnt += 1
            else:
                nums[idx - cnt] = nums[idx]
        print(nums)
        return len(nums) - cnt