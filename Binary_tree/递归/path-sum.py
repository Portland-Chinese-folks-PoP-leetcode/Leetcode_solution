# https://leetcode.cn/problems/path-sum/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, top):
            if root == None:
                return False
            cur_val = root.val+top
            if cur_val == targetSum and root.left == None and root.right == None:
                return True
            return traverse(root.left, cur_val) or traverse(root.right, cur_val)
        if root == None:
            return False
        res = traverse(root, 0)
        return res
