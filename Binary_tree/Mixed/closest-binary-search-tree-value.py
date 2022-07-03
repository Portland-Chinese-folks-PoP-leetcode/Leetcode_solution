# https://leetcode.cn/problems/closest-binary-search-tree-value/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    min_abs = math.inf
    res = None

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        res = None

        def traverse(root):
            if root == None:
                return
            if abs(root.val-target) < self.min_abs:

                self.res = root.val
                self.min_abs = abs(root.val-target)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.res


# 这个可以用二分也可以和230一样用中序

# 下面是稍微改进一下利用一下bst的性质

class Solution:
    min_abs = math.inf
    res = None

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        res = None

        def traverse(root):
            if root == None:
                return
            if abs(root.val-target) < self.min_abs:

                self.res = root.val
                self.min_abs = abs(root.val-target)
            if root.val > target:
                traverse(root.left)
            else:
                traverse(root.right)
        traverse(root)
        return self.res
