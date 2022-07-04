# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def traverse(rootA, rootB):
            if rootA == None and rootB == None:
                return True
            if rootA == None or rootB == None:
                return False
            if rootA.val != rootB.val:
                return False
            return traverse(rootA.left, rootB.left) and traverse(rootA.right, rootB.right)

        return traverse(p, q)
# https://leetcode.cn/problems/same-tree
