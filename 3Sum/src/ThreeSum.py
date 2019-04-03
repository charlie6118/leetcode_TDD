class Solution(object):
    def threeSum(self, nums):
        aux = nums.copy()
        pairList = []
        for index, num in enumerate(nums):
            for j in range(index + 1, len(nums)):
                pairList.append((aux[j], num))

        result = []
        for (x, y) in pairList:
            nums.remove(x)
            nums.remove(y)
            for num in nums:
                if (x + y) == - num:
                    if x <= y <= num and [x, y, num] not in result:
                        result.append([x, y, num])
                    if x <= num <= y and [x, num, y] not in result:
                        result.append([x, num, y])
                    if num <= x <= y and [num, x, y] not in result:
                        result.append([num, x, y])
                    if num <= y <= x and [num, y, x] not in result:
                        result.append([num, y, x])
                    if y <= x <= num and [y, x, num] not in result:
                        result.append([y, x, num])
                    if y <= num <= x and [y, num, x] not in result:
                        result.append([y, num, x])
            nums.append(x)
            nums.append(y)
        return result

        # resultFinal = []
        # for r in result:
        #     r.sort()
        #     if r not in resultFinal:
        #         resultFinal.append(r)
        # return resultFinal

S = Solution()
print(S.threeSum([-1, 0, 1, 2, -1, -4]))