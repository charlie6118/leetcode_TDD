class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        c1, c2, cnt1, cnt2 = 0, 0, 0, 0
        
        # if a pair of nums are not the same then discard both
        for n in nums:
            if c1 == n:
                cnt1 += 1
            elif c2 == n:
                cnt2 +=1
            elif cnt1 == 0:
                c1, cnt1 = n, 1
            elif cnt2 == 0:
                c2, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        r = []
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == c1:
                cnt1 += 1
            elif n == c2:
                cnt2 += 1
        if cnt1 > len(nums) // 3:
            r.append(c1)
        if cnt2 > len(nums) // 3:
            r.append(c2)
        return r

        # n = len(nums) // 3
        # d = {}
        # r = set()
        # for num in nums:
        #     d[num] = d.get(num, 0) + 1
        #     if d[num] > n:
        #         r.add(num)
        # return list(r)