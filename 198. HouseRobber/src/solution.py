class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Thanks for the great tutorial from Max Manzhos
        # https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.

        now, pre = 0, 0
        for n in nums:
            temp = now
            now = max(now, pre + n)
            pre = temp
        return now


        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return nums[0]
        # dp = [0] * (len(nums) + 1)
        # dp[1] = nums[0]
        # dp[2] = max(nums[0], nums[1])
        
        # for idx in range(2, len(nums) + 1):
        #     dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx - 1])
        # return dp[-1]