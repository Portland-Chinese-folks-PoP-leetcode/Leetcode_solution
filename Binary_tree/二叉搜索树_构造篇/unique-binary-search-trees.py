class Solution:
    def numTrees(self, n: int) -> int:
        def count(low, high):
            if low > high:
                return 1
            res = 0
            for i in range(low, high+1):
                left = count(low, i-1)
                right = count(i+1, high)
                res = res + left*right
                print(res)
            return res
        return count(1, n)


a = Solution()
a.numTrees(3)
