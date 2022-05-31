#https://leetcode-cn.com/problems/number-of-distinct-islands
class Solution:
    def numDistinctIslands(self, grid) -> int:

        def island_dfs(grid, i, j, sb, dir):
            m = len(grid)
            n = len(grid[0])
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            sb.append(str(dir))
            island_dfs(grid, i-1, j, sb, 1)
            island_dfs(grid, i+1, j, sb, 2)
            island_dfs(grid, i, j-1, sb, 3)
            island_dfs(grid, i, j+1, sb, 4)
            sb.append(str('-'+str(dir)))

        m = len(grid)
        n = len(grid[0])
        island = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sb = []
                    island_dfs(grid, i, j, sb, '1')

                    island[str(sb)] = str(sb)

        return len(island)
    
    
aaa=[1.,2,4,5,6]
print(str(aaa))
