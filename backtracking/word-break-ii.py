from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        track = []
        res = []

        def backtrack(start, track):
            if start == len(s):
                res.append(' '.join(map(str, track)))
                return
            if start > len(s):
                return
            for word in wordDict:
                length = len(word)
                if start+length > len(s):
                    continue
                substring = s[start:start+length]
                if substring != word:
                    continue
                track.append(word)
                backtrack(start+length, track)
                track.pop(-1)
        backtrack(0, track)
        return res
