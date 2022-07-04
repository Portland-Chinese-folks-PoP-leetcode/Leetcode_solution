# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math


class Solution(object):
    depth = 0

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        q = deque()
        q.append(root)
        while len(q) > 0:
            size = len(q)
            self.depth += 1
            for i in range(size):
                cur = q.popleft()
                if cur.left is None and cur.right is None:
                    return self.depth
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
