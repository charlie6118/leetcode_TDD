class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for idx in range(2, len(nums) + 1):
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx - 1])
        return dp[-1]