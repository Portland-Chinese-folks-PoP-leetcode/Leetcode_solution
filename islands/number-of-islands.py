class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # This is a simple framework demo for island
        def dfs(grid: List[List[str]], i: int, j: int):
            m = len(grid)  # row的长度
            n = len(grid[0])  # column 的长度
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid, i-1, j)  # 遍历上方
            dfs(grid, i+1, j)  # 遍历下方
            dfs(grid, i, j-1)  # 遍历左边
            dfs(grid, i, j+1)  # 遍历右边

        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
        return res
