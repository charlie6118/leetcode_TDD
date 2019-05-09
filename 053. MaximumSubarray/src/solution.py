class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [nums[0]] * (len(nums) + 1)
        max_v = nums[0]
        
        for idx in range(1, len(nums)):
            dp[idx] = max(nums[idx], nums[idx] + dp[idx - 1])
            max_v = max(max_v, dp[idx])
        return max_v