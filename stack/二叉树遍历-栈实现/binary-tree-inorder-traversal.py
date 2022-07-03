# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque()
        res = []
        while root is not None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
