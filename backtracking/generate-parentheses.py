class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        track = []
        res = []
        left = 0
        right = 0

        def backtrack(left, right):
            if left < right:
                return
            if left > n or right > n:
                return
            if left == n and right == n:
                track_string = ''.join(map(str, track))
                res.append(track_string)
            track.append('(')
            backtrack(left+1, right)
            track.pop(-1)

            track.append(')')
            backtrack(left, right+1)
            track.pop(-1)
        backtrack(left, right)
        return res

# https://leetcode-cn.com/problems/generate-parentheses/submissions/
# 在这题中我找到了一中全新的把list变成 string的方式
