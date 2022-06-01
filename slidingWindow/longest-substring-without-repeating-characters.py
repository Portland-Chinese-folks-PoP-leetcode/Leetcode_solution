class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {i: 0 for i in s}
        left, right, res = 0, 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            while window[c] > 1:  # 代表滑动窗口中有重复的元素
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right-left)
        return res
