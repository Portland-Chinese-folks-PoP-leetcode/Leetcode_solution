# https://leetcode-cn.com/problems/number-of-1-bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n is not 0:
            n = n & (n-1)
            res += 1
        return res


aaa = 4
