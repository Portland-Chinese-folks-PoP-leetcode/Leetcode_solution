# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    res = 0

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def traverse(root):  # 定义 如果是binary search tree。返回root和他自己的节点数
            if root == None:
                return [math.inf, -math.inf, 0]
            left = traverse(root.left)
            right = traverse(root.right)
            if left == None or right == None:
                return None
            left_min, left_max, leftCount = left[0], left[1], left[2]
            right_min, right_max, rightCount = right[0], right[1], right[2]
            if root.val > left_max and root.val < right_min:
                #这种情况下一定是二叉树，并且在root没有left或者right的时候也能够得以判断
                rootMin = min(left_min, root.val)
                rootMax = max(right_max, root.val)
                rootCount = leftCount+rightCount+1
                self.res = max(self.res, rootCount)
                return [rootMin, rootMax, rootCount]
            return None
        traverse(root)
        return self.res
