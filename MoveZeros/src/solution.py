class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeroIdx = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[zeroIdx] = nums[zeroIdx], nums[i]
                zeroIdx += 1
        return


        # n = len(nums)
        # cnt = 0
        # for i in range(n):
        #     if nums[i] == 0:
        #         cnt += 1
        #         nums.append(0)
        # print(nums[:n], nums[n: n + 1 + cnt])     
        # tmp = list(filter(None, nums))
        # return tmp + nums[n: n + 1 + cnt]