# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque()
        while root != None or len(stack) > 0:
            while root is not None:
                res.append(root.val)  # 根
                stack.append(root)
                root = root.right  # 右
            cur = stack.pop()
            root = cur.left  # 左
        res.reverse()
        return res


wl
