# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# binary search tree的构造 还挺难的
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def build(low, high):
            res = []
            # base case
            if low > high:
                res.append(None)
                return res
            #  1、穷举 root 节点的所有可能。
            for i in range(low, high+1):
                # 2、递归构造出左右子树的所有合法 BST。
                left_tree = build(low, i-1)
                right_tree = build(i+1, high)
                # 3、给 root 节点穷举所有左右子树的组合。
                for left in left_tree:
                    for right in right_tree:
                        #  i 作为根节点 root 的值
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        if n == 0:
            return []
        return build(1, n)
