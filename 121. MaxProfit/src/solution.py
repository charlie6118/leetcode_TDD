class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        lower_bound = prices[0]
        dp = [0] * (len(prices) + 1)
        for i in range(1, len(prices)):
            lower_bound = min(lower_bound, prices[i])
            dp[i] = prices[i] - lower_bound
        return max(dp)