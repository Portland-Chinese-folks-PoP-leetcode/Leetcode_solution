# https://leetcode.cn/problems/longest-palindromic-substring/submissions/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s: str, l: int, r: int):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        res = ''
        for i in range(0, len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i+1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2

        return res
