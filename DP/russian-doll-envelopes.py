

def maxEnvelopes(envelopes) -> int:
    if not envelopes:
        return 0
    n = len(envelopes)
    # 这一部很巧妙，有用到 lanbda也用到了 sort的参数控制
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if envelopes[j][1] < envelopes[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


#envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
envelope2 = [[1, 8], [2, 3], [5, 4], [5, 2], [6, 4], [6, 7]]

# envelope2 = sorted(envelope2, key=lambda x: x[0])
# ss = sorted(envelope2, key=lambda x: -x[1])
# print(ss)
print(maxEnvelopes(envelope2))

help(envelope2.sort)

# def key(x): return (x[0], -x[1])
