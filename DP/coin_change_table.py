
# 函数定义：凑出总金额 amount， 至少需要coinChange(coins,amount)枚 硬币
# dp数组定义:凑出金额i(索引)，还少需要dp[i]枚硬币

def coinChange(coins,amount):
    # dp数组的初始化，这时候可以初始化成最大值
    # 如果题目让你 求最小值，dp数组可以初始化成最大值，
    # 反之亦然
    dp=[amount+1]*(amount+1)
    print(dp)
    dp[0]=0
    for i in range(0,len(dp)):
        for coin in coins:
            if i- coin <0: continue
            # 状态转移
            # 这个题目一定是自底向上的，所以把金额9，6，10的硬币个数加1，再求他们的最小值
            dp[i]=min(dp[i],1 + dp[i - coin])
    if dp[amount]==amount + 1:
        return -1
    else:
        return dp[amount]
    
coins=[1,2,5]

print(coinChange(coins,20))
    

