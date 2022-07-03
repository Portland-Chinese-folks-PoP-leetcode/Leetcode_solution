# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import heapq


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inOrder(root):
            stack = deque()
            res = []
            while root is not None or len(stack) > 0:
                while root is not None:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                res.append(root.val)
                root = root.right
            return res
        res = inOrder(root)
        q = []
        for i in res:
            heapq.heappush(q, (abs(target-i), i))
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(q)[1])
        return answer
