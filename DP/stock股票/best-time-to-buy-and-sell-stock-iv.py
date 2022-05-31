# https: // leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/submissions/
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # def maxProfit_k_inf(prices):
        #     n = len(prices)
        #     dp = [[0 for i in range(n)] for j in range(2)]
        #     for i in range(n):
        #         if i-1 == -1:
        #             dp[0][i] = 0
        #             dp[1][i] = -prices[i]
        #             continue
        #         dp[0][i] = max(dp[0][i-1], dp[1][i-1]+prices[i])
        #         dp[1][i] = max(dp[1][i-1], dp[0][i-1]-prices[i])
        #     return dp[0][n-1]
        max_k = k
        n = len(prices)
        if n == 0:
            return 0
        # if max_k>n/2:
        #     return maxProfit_k_inf(prices)
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
