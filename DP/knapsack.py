# dp[i][j]的定义 对于钱i个物品，当前背包的容量为w，这种情况下可以装的最大值
# 定性二维数组的动态规划 非常 非常难


def knapsack(W, N, wt, value):
    dp = [[0 for i in range(0, W+1)] for j in range(N+1)]
    for i in range(1, N+1):
        # print('current i is ', i)
        for w in range(1, W+1):
            # print('current w is ', w)
            # print('currenmt dp[i][w] is ', i, w, dp[i][w])
            # print('current wt[i-1] is',  wt[i-1])
            if w - wt[i-1] < 0:
                # print('这种情况下只能选择不装入背包')
                dp[i][w] = dp[i-1][w]
            else:
                # print('选择')
                dp[i][w] = max(dp[i - 1][w - wt[i-1]] + val[i-1], dp[i - 1][w])
            # print(dp)
    return dp[N][W]


N = 3
W = 4
wt = [2, 1, 3]
val = [4, 2, 3]

print(knapsack(W, N, wt, val))
