#https://leetcode.cn/problems/minimum-window-substring/submissions/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {c: 0 for c in t}
        window = {c: 0 for c in s}
        for c in t:
            need[c] += 1
        left, right, valid, start = 0, 0, 0, 0
        length = math.inf
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            """当 valid == need.size() 时，说明 T 中所有字符已经被覆盖，
            已经得到一个可行的覆盖子串，现在应该开始收缩窗口了"""
            while valid == len(need):
                # 在这里更新最小覆盖子串,判断当前的最小覆盖的长度是否比之前的小
                if right-left < length:
                    start = left
                    length = right-left
                # d 是将移出窗口的字符
                d = s[left]  # d is the cahr that gonna be moved out of the window
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        if length == math.inf:
            return ''
        else:
            return s[start:start+length]
