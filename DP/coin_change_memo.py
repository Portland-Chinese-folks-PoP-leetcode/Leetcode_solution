# https://labuladong.github.io/algo/3/24/70/

# 状态： 目标金额 amount
# 选择： coins数组中列出的所有金额的面额
# 函数定义：凑出总金额 amount， 至少需要coinChange(coins,amount)枚 硬币
# base case ， amount =0 时，需要0枚硬币，amount<0 时，不可能凑出
def coinchange(coins, amount):
    memo = {}

    def dp(coins: list, amount: int):
        # base case
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = 10000

        if amount in memo:
            return memo[amount]
        for coin in coins:
            # 计算子问题的结果
            subProblem = dp(coins, amount-coin)
            # 子问题无解则跳过
            if subProblem == -1:
                continue
            # 在子问题中选择最优解，然后加1
            res = min(res, subProblem+1)

        if res == 10000:
            memo[amount] = res
            return -1
        else:
            memo[amount] = res
            return res

    return dp(coins, amount)


def dp(coins: list, amount: int):
    # base case
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    res = 10000

    if amount in memo:
        return memo[amount]
    for coin in coins:
        # 计算子问题的结果
        subProblem = dp(coins, amount-coin)
        # 子问题无解则跳过
        if subProblem == -1:
            continue
        # 在子问题中选择最优解，然后加一
        res = min(res, subProblem+1)

    if res == 10000:
        return -1
    else:
        memo[amount] = res
        return res


coins = [1, 2, 5]

print(coinchange(coins, 19))
