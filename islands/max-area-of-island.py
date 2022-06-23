class Solution:
    def maxAreaOfIsland(self, grid):
        def island_dfs(grid, i, j):
            m = len(grid)
            n = len(grid[0])
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            return island_dfs(grid, i+1, j) + island_dfs(grid, i, j+1) + island_dfs(grid, i-1, j) + island_dfs(grid, i, j-1) + 1
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                print('current i is', i)
                print('current j is ', j)
                if grid[i][j] == 1:
                    print('grid ', i, j, 'is ', 1)
                    res = max(res, island_dfs(grid, i, j))

                    print(res)
        return res


a = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
a.maxAreaOfIsland(grid)



#### 下面是第二次做这个题目
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if i >= m or j >= n or i < 0 or j < 0:  # 这一行一定要在 grid[i][j]==0 的前面
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return dfs(grid, i-1, j)+dfs(grid, i+1, j)+dfs(grid, i, j-1)+dfs(grid, i, j+1)+1
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(grid, i, j))
        return res
