def min_distance(s1: str, s2: str):
    memo = dict()

    def dp(i, j):
        if i == -1:
            return j+1
        if j == -1:
            return i+1
        print(memo)
        if (i, j) in memo:
            return memo[(i, j)]
        if s1[i] == s2[j]:
            memo[(i, j)] = dp(i-1, j-1)

        else:
            # 状态的转移方程
            memo[(i, j)] = min(dp(i-1, j)+1, dp(i, j-1)+1, dp(i-1, j-1)+1)
        return memo[(i, j)]

    return dp(len(s1)-1, len(s2)-1)


s1 = 'exponential'
s2 = 'polynomial'

print(min_distance(s1, s2))
