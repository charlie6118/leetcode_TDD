class Solution:
    def singleNumber(self, nums) -> int:
        return 2 * sum(set(nums)) - sum(nums)
    
    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res