class Solution:
    memo = {}

    def numTrees(self, n: int) -> int:
        def count(low, high):
            if low > high:
                return 1
            res = 0  # 这个res在nest function count 里面的原因就是 每一层（固定node数量的bst）都有自己的数量的树形状的排列，如果这个res在外面就变成了 子集的数量
            if (low, high) in self.memo:
                return self.memo[(low, high)]

            for i in range(low, high+1):  # 1、穷举 root 节点的所有可能。
                # 2、递归构造出左右子树的所有可能出现的数量
                left = count(low, i-1)
                right = count(i+1, high)
                res = res + left*right  # 给 root 节点穷举所有左右子树的组合
            self.memo[(low, high)] = res  # 将结果存入备忘录
            return res
        return count(1, n)

# 下面是讲解


class Solution:
    # count = 0

    # def printIndent(self, n):
    #     print("    "*n, end=' ')

    def numTrees(self, n: int) -> int:

        def count(low, high):
            # self.count += 1
            # self.printIndent(self.count)
            # print('low is ', low, 'high is ', high)
            if low > high:

                # self.printIndent(self.count)
                # self.count = self.count-1
                # print('return 1')
                return 1
            res = 0
            if (low, high) in self.memo:
                return self.memo[(low, high)]
            for i in range(low, high+1):
                # i 的值作为根节点 root
                left = count(low, i-1)
                right = count(i+1, high)
                # 左右子树的组合数乘积是 BST 的总数
                res = res + left*right
            # self.printIndent(self.count)
            # self.count = self.count-1
            # print('left is ', left, ', right is ', right, end=' ')
            # print('return val is res, res is ', res)
            self.memo[(low, high)] = res
            return res
        return count(1, n)


a = Solution()
a.numTrees(2)
