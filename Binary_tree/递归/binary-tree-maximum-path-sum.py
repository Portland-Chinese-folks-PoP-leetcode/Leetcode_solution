# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_val = -inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root == None:
                return 0
            left_max = max(0, traverse(root.left))
            right_max = max(0, traverse(root.right))
            pathMaxSum = root.val+left_max+right_max
            self.max_val = max(self.max_val, pathMaxSum)
            return max(left_max, right_max)+root.val
        if root == None:
            return 0
        traverse(root)
        return self.max_val
