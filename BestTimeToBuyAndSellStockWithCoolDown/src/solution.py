class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
        
        if len(prices) < 2:
            return 0
        s0 = [0] * len(prices) # Can buy
        s1 = [0] * len(prices) # Can sell
        s2 = [0] * len(prices) # Need rest
        s1[0] = -prices[0]
        i = 0
        for i in range(1, len(prices)):
            s0[i] = max(s2[i - 1], s0[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]
        
        return max(s2[-1], s0[-1])