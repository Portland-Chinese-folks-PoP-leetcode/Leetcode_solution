# This is a simple framework demo for island
def dfs(grid: List[List[str]], i: int, j: int, visited: List[List[boolean]]):
    m = len(grid)  # row的长度
    n = len(grid[0])  # column 的长度
    if i < 0 or j < 0 or i >= m or j >= n:
        return
    if visited[i][j]:
        return
    visited[i][j] = True
    dfs(grid, i-1, j, visited)  # 遍历上方
    dfs(grid, i+1, j, visited)  # 遍历下方
    dfs(grid, i, j-1, visited)  # 遍历左边
    dfs(grid, i, j+1, visited)  # 遍历右边
