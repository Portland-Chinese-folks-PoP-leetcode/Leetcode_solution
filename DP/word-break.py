class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if s[i:j] in wordDict and dp[i] == True:
                    dp[j] = True
        return dp[-1]
