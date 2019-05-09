class Solution:
    def reverse(self, x: int) -> int:
        plusOrMinus = 1
        if x < 0:
            x = abs(x)
            plusOrMinus = -1
        r = 0
        while x > 0:
            r = 10 * r + x % 10
            x = x // 10
        if r * plusOrMinus > 2 ** 31 - 1 or r * plusOrMinus < -(2 ** 31):
            return 0
        return (r) * plusOrMinus
