# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_k = 2
        n = len(prices)
        dp = [[[0 for i in range(n)] for j in range(max_k+1)]for k in range(2)]
        for i in range(n):
            for k in range(max_k, 0, -1):
                if i-1 == -1:
                    dp[0][k][i] = 0
                    dp[1][k][i] = -prices[i]
                    continue
                dp[0][k][i] = max(dp[0][k][i-1], dp[1][k][i-1]+prices[i])
                dp[1][k][i] = max(dp[1][k][i-1], dp[0][k-1][i-1]-prices[i])

        return dp[0][max_k][n-1]
