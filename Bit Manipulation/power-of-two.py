class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n & (n-1) == 0:
            return True
        return False
# https://leetcode-cn.com/problems/power-of-two/submissio
