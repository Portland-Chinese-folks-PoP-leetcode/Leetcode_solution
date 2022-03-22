#https://labuladong.github.io/algo/3/24/70/

def coinchange(coins,amount):
    return dp(coins,amount)

def dp(coins:list,amount:int):
    # base case
    if amount==0: return 0
    if amount<0: return -1
    res=10000
    memo={}
    if amount in memo:
        return memo[amount]
    for coin in coins:
        #计算子问题的结果
        subProblem=dp(coins,amount-coin)
        #子问题无解则跳过
        if subProblem==-1: continue
        #在子问题中选择最优解，然后加一
        res=min(res,subProblem+1)
            
    if res==10000:
        return -1
    else:
        memo[amount]=res
        return res
    
coins=[1,2,5]

print(coinchange(coins,8))
