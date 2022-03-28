#
# 这种题目中给定给的钱 只能弄用一次biru geiding  1,2,5,20面值的草票，这些草票在一次找钱中只能使用一次
# 这个解法肯定是有问题的所以先不要管
def make_chang(coins, value):
    # print(coins)
    memo = {}

    def dp(coins, value):
        print(memo)
        if value == 0:
            return True
        if value in memo:
            return memo[value]
        else:
            for coin in coins:
                # coinx = coins
                # coinx = coinx.remove(coin)
                coins.remove(coin)
                res = make_chang(coins, value-coin)
                coins.append(coin)
                if res == True:
                    memo[value] = True
                    return True
            memo[value] == False
            return False
    return dp(coins, value)


value = 31
coins = [1, 5, 10, 20]

print(make_chang(coins, value))
