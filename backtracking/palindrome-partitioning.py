from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                print('    i is ', i, 'j is ', j)
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        res = list()
        track = list()

        def dfs(start: int):
            print(track)
            if start == n:
                res.append(track[:])
                return

            for j in range(start, n):
                if dp[start][j]:
                    track.append(s[start:j+1])
                    dfs(j + 1)
                    track.pop()

        dfs(0)
        return res


s = Solution()
s.partition("aab")
