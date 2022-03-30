class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)  # i 从上 往下遍历， 表示行数
        m = len(grid[0])  # j 从左往右遍历，表示列数
        dp = [[inf for i in range(0, m+1)] for _ in range(0, n+1)]
        dp[0][1] = 0
        dp[1][0] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = min(dp[i-1][j]+grid[i-1][j-1],
                               dp[i][j-1]+grid[i-1][j-1])
        return dp[n][m]

# test case [[1,3,1],[1,5,1],[4,2,1]]
