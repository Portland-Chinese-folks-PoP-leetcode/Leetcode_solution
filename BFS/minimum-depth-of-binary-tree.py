# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 1
        q = []
        q.append(root)

        while len(q) > 0:
            size = len(q)
            for i in range(size):
                current = q.pop(0)
                if current.left is None and current.right is None:
                    return depth
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            depth += 1
        return depth
