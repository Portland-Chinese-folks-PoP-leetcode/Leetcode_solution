class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[True for i in range(n)] for j in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if dp[i][j] == True:
                    res += 1
        return res

# https://leetcode.cn/problems/palindromic-substrings/submissions/
