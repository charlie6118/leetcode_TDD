class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1] * (n + 1)
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]