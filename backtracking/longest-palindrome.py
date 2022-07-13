# It's not backtracking but it shows how to use a Counter from collections
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        print(counter)
        res = 0
        max_odd_len = 0
        isodd = False
        for i in counter:
            if counter[i] % 2 == 0:
                res += counter[i]
            else:
                isodd = True
                res += counter[i]-1  # 当是odd的情况下的时候加入该字母数的偶数个
                # max_odd_len=max(max_odd_len,counter[i])

        if isodd == False:
            return res
        else:
            return res+1
# https://leetcode.cn/problems/longest-palindrome/submissions/
