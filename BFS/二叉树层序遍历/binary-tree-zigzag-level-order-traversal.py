# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/submissions/
# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """ When I first look at this question I recognize several features that this question has
        the data structure is a binary tree. and the elements of the output list is  a list of ndoe on breanth level of the binary tree.
        So I would like to use breath first search approach to over come this question。 First I'm gonna define a queue  this queue contains the node of next level
        """
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
