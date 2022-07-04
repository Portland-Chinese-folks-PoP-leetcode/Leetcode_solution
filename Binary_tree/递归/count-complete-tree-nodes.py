# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
# 其实不一定需要使用 math，因为pow是python的内置函数
# https://leetcode.cn/problems/count-complete-tree-nodes/

class Solution:

    def countNodes(self, root: TreeNode) -> int:
        left_node = root
        right_node = root
        leftHeight = 0
        rightHeight = 0
        while left_node is not None:
            left_node = left_node.left
            leftHeight += 1
        while right_node is not None:
            right_node = right_node.right
            rightHeight += 1
        if leftHeight == rightHeight:
            return int(math.pow(2, leftHeight)-1)
        return int(1+self.countNodes(root.left)+self.countNodes(root.right))
