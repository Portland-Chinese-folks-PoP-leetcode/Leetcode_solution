class Solution:
    count = 0

    def printIndent(self, n):
        print("    "*n, end=' ')

    def numTrees(self, n: int) -> int:

        def count(low, high):
            self.count += 1
            self.printIndent(self.count)
            print('low is ', low, 'high is ', high)
            if low > high:

                self.printIndent(self.count)
                self.count = self.count-1
                print('return 1')
                return 1
            res = 0
            for i in range(low, high+1):
                left = count(low, i-1)
                right = count(i+1, high)
                res = res + left*right

            self.printIndent(self.count)
            self.count = self.count-1
            print('left is ', left, ', right is ', right, end=' ')
            print('return val is res, res is ', res)

            return res
        return count(1, n)


a = Solution()
a.numTrees(2)
