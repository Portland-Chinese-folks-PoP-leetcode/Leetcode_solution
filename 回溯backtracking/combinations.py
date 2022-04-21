class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(start, k):

            if len(track) == k:

                res.append(list(track))
                return
            for i in range(start, n+1):
                track.append(i)
                backtrack(i+1, k)
                track.pop(-1)
        track = []
        res = []
        backtrack(1, k)
        return res

# https://leetcode-cn.com/problems/combinations/
