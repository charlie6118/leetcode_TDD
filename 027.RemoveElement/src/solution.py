class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        cnt = 0
        for n in nums:
            if n != val:
                nums[cnt] = n
                cnt += 1
        nums = nums[:cnt]
        return cnt
        