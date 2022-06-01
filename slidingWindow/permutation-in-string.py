# https://leetcode.cn/problems/permutation-in-string/submissions/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {i: 0 for i in s1}
        window = {i: 0 for i in s2}
        for c in s1:
            need[c] += 1
        left, right, valid = 0, 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while right-left >= len(s1):
                #在这里判断是否找到了合法的子串
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
