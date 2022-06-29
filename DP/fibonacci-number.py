# memorization
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n-1)+self.fib(n-2)

# tabulation


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        dp = [0 for i in range(n+1)]
        dp[0], dp[1] = 0, 1
        for i in range(2, len(dp)):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
