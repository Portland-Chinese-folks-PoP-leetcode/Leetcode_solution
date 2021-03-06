def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 0
    case1 = longestPalindromeSubseq(s[1:])
    case2 = longestPalindromeSubseq(s[:-1])
    case3 = longestPalindromeSubseq(s[1:-1])
    print(case1, case2, case3)
    biggest = max(case1, case2, case3)

    if s[0] == s[-1]:
        return 2+max(case1, case2, case3)
    else:
        return max(case1, case2, case3)


def lps(seq, i, j):

    # Base Case 1: If there is
    # only 1 character
    if (i == j):
        return 1

    # Base Case 2: If there are only 2
    # characters and both are same
    if (seq[i] == seq[j] and i + 1 == j):
        return 2

    # If the first and last characters match
    if (seq[i] == seq[j]):
        return lps(seq, i + 1, j - 1) + 2

    # If the first and last characters
    # do not match
    return max(lps(seq, i, j - 1),
               lps(seq, i + 1, j))


# dp 数组的定义是 dp[i][j]=x的定义是，string[i:j]内的最长回文子序列的长度
# 所以这个题目迭代的时候要从最后开始迭代，j却要从 range(i+1，n)内迭代。
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):  # 这一步至关重要 是在初始化的位置在对角线上的元素
            dp[i][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]


string = 'baab'

print(longestPalindromeSubseq_table(string))

string2 = 'abwttw'
n = len(string2)
for i in range(n-1, -1, -1):
    print(string[i])
