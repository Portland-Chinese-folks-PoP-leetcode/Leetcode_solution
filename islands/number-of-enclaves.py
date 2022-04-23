class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(grid: List[List[int]], i: int, j: int):
            m: int = len(grid)
            n: int = len(grid[0])
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)

        m: int = len(grid)
        n: int = len(grid[0])
        res: int = 0
        for j in range(n):
            dfs(grid, 0, j)
            dfs(grid, m - 1, j)

        for i in range(m):
            dfs(grid, i, 0)
            dfs(grid, i, n - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1

        return res
