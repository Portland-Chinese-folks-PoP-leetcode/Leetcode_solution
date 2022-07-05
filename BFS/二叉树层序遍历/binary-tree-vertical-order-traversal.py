# https://leetcode.cn/problems/binary-tree-vertical-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, OrderedDict


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if root == None:
            return res
        m = OrderedDict()
        q = deque()
        q.append((root, 0))
        while len(q) > 0:
            size = len(q)
            for i in range(size):
                cur = q[0][0]
                level = q[0][1]
                if level not in m:
                    m[level] = [cur.val]
                else:
                    m[level].append(cur.val)
                q.popleft()
                if cur.left:
                    q.append((cur.left, level-1))
                if cur.right:
                    q.append((cur.right, level+1))
        res = []
        for i in sorted(m.keys()):
            res.append(m[i])
        return res
