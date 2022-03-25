def longestCommonSubsequence(text1, text2):
    N = len(text1)
    M = len(text2)
    print(N, M)
    # N is column J is row we alway iter rate by row
    dp = [[0 for i in range(N+1)] for j in range(M+1)]

    for j in range(1, M+1):
        for i in range(1, N+1):
            print('')
            if text2[j-1] == text1[i-1] and dp[j-1][i]+1 <= j:

                dp[j][i] = dp[j-1][i-1]+1

            else:
                dp[j][i] = max(dp[j][i-1], dp[j-1][i])
            print(dp)
    return dp[M][N]


text1 = "ade"

text2 = "abcde"


print(longestCommonSubsequence(text1, text2))
print('test case 2----- \n \n \n ')
# text3 = "bl"
# text4 = "yby"
# print(longestCommonSubsequence(text3, text4))


# def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#      m, n = len(text1), len(text2)
#       dp = [[0] * (n + 1) for _ in range(m + 1)]

#        for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if text1[i - 1] == text2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1] + 1
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

#         return dp[m][n]

