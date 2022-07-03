# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
"""
我的版本是取到bfs的每一层的最后一个element
"""
# https://leetcode.cn/problems/binary-tree-right-side-view/submissions/


class Solution:
    # 所谓在右侧的能看到的节点
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        q = deque()
        q.append(root)
        res = [root.val]
        while len(q) > 0:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if len(q) > 0:
                res.append(q[-1].val)
        return res


### 改进版本 


class Solution:
    #所谓在右侧的能看到的节点
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        q = deque()
        q.append(root)
        res = []
        while len(q) > 0:
            size = len(q)
            last = q[0]
            for i in range(size):
                cur = q.popleft()
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)

            res.append(last.val)
        return res
