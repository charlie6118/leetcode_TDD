class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            if height[l] < height[r]:
                tmp = (r - l) * height[l]
                l += 1
            else:
                tmp = (r - l) * height[r]
                r -= 1
            max_water = max(max_water, tmp)
        return max_water