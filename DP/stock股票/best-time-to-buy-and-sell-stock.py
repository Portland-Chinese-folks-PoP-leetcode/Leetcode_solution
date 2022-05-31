# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
# maxProfit_k_1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(n)] for j in range(2)]
        print(dp)
        for i in range(n):
            if i - 1 == -1:
                dp[0][i] = 0
                dp[1][i] = -prices[i]
                continue
            dp[0][i] = max(dp[0][i-1], dp[1][i-1]+prices[i])
            dp[1][i] = max(dp[1][i-1], -prices[i])
        return dp[0][n-1]
