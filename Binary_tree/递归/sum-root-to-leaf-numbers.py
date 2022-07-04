# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0

    def sumNumbers(self, root: TreeNode) -> int:
        def traverse(root, path):
            if root == None:
                return
            if root.left == None and root.right == None:
                path.append(root.val)
                self.res += int(''.join(map(str, path)))
                path.pop(-1)
                return
            path.append(root.val)
            traverse(root.left, path)
            path.pop(-1)
            path.append(root.val)
            traverse(root.right, path)
            path.pop(-1)
        path = []
        traverse(root, path)
        return self.res
