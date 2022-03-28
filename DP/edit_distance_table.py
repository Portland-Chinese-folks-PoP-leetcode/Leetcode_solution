from numpy import *

# 这个题目考查的内容是 把word1变成word2 需要几步
# dp[i][j]是 s1[0,i],s2[0,j]的最小编辑距离


def min_edit_distance(s1: str, s2: str):
    m = len(s1)
    n = len(s2)
    dp = [[i for i in range(0, m+1)] for _ in range(0, n+1)]
    print(dp)
    for i in range(0, n+1):
        dp[i][0] = i

    for i in range(1, n+1):  # 遍历的是行 从上往下
        for j in range(1, m+1):  # 遍历的是列，从左往右
            # print(i, j)
            # print(s2, s2[i-1])
            # print(s1, s1[j-1])

            if s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
                # 删除 dp[i][j-1]+1
                # 插入 dp[i-1][j]+1
                # 替换 dp[i-1][j-1]+1
            # print(dp)
    return dp[n][m]


s1 = 'horse'

s2 = 'ros'

print(min_edit_distance(s1, s2))

print(float(inf))
print(1 < inf)
