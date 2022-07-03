# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        q = deque()
        q.append(root)
        Zigzag = 1
        res = []
        while len(q) > 0:
            size = len(q)
            level = deque()
            for i in range(size):
                cur = q.popleft()
                if Zigzag % 2 == 1:
                    level.append(cur.val)
                else:
                    level.appendleft(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(list(level))
            Zigzag += 1
        return res
