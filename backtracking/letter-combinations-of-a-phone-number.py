from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        phone = ['', '', 'abc', 'def', 'ghi',
                 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        track = []

        def backtrack(track, start, digits):

            if len(track) == len(digits):
                res.append(''.join(map(str, track)))
                return
            for i in range(start, len(digits)):
                alps = phone[int(digits[i])]
                for c in alps:
                    track.append(c)
                    backtrack(track, i+1, digits)
                    track.pop(-1)
        backtrack(track, 0, digits)
        if len(digits) == 0:
            return []
        return res


tc1 = "23"
s = Solution()
s.letterCombinations(tc1)
