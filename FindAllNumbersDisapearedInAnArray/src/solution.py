class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = - abs(nums[idx])
            print(nums)
        r = []
        for i, v in enumerate(nums):
            if v > 0:
                r.append(i + 1)
        return (r)