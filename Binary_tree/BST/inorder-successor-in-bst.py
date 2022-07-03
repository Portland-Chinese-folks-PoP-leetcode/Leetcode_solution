# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = []
        stack = deque()
        node_res = []
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            node_res.append(root)
            root = root.right
        idx = res.index(p.val)
        if p.val == max(res):
            return None
        else:
            return node_res[idx+1]
