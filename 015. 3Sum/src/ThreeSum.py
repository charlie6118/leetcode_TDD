class Solution(object):
    def threeSum(self, nums):
        result = set()
        plus = sorted([num for num in nums if num > 0])
        plus_s = set(plus)
        minus = sorted([num for num in nums if num < 0])
        minus_s = set(minus)
        zero = [num for num in nums if num == 0]
        # 0, 0, 0
        if len(zero) > 2:
            result.add((0, 0, 0))
        # -, 0, +
        if len(zero) > 0:
            for e in plus_s:
                if -e in minus_s:
                    result.add((-e, 0, e))
        # -, -, +
        lenM = len(minus)
        for i in range(lenM):
            for j in range(i + 1, lenM):
                sumTwoMinus = minus[i] + minus[j]
                if -sumTwoMinus in plus_s:
                    result.add((minus[i], minus[j], -sumTwoMinus))
        # -, +, +
        lenP = len(plus)
        for i in range(lenP):
            for j in range(i + 1, lenP):
                sumTwoPlus = plus[i] + plus[j]
                if -sumTwoPlus in minus_s:
                    result.add((-sumTwoPlus, plus[i], plus[j]))
        return list(result)
S = Solution()
print(S.threeSum([-1, 0, 1, 2, -1, -4]))