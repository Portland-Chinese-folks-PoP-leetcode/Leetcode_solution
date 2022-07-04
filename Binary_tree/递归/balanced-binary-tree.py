# https://leetcode.cn/problems/balanced-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = True

    def isBalanced(self, root: TreeNode) -> bool:
        def traverse(root):
            if root == None:
                return 0  # return height
            left = traverse(root.left)
            right = traverse(root.right)
            if abs(left-right) > 1:
                self.res = False
            return max(left, right)+1
        traverse(root)
        return self.res
