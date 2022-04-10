# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# binary search tree的构造 还挺难的
class Solution:
    res = []

    def generateTrees(self, n: int) -> List[TreeNode]:
        def build(low, high):
            res = []
            if low > high:
                res.append(None)
                return res
            for i in range(low, high+1):
                left_tree = build(low, i-1)
                right_tree = build(i+1, high)
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        if n == 0:
            return []
        return build(1, n)
