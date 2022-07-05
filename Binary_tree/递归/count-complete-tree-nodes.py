# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
# 其实不一定需要使用 math，因为pow是python的内置函数
# https://leetcode.cn/problems/count-complete-tree-nodes/
# https://labuladong.github.io/algo/2/20/46/ 很牛逼的讲解


class Solution:

    def countNodes(self, root: TreeNode) -> int:
        left_node = root
        right_node = root
        # 沿最左侧和最右侧分别计算高度
        leftHeight = 0
        rightHeight = 0
        while left_node is not None:
            left_node = left_node.left
            leftHeight += 1
        while right_node is not None:
            right_node = right_node.right
            rightHeight += 1
        # 如果左右侧计算的高度相同，则是一棵满二叉树
        if leftHeight == rightHeight:
            return int(math.pow(2, leftHeight)-1)
        # 如果左右侧的高度不同，则按照普通二叉树的逻辑计算
        return int(1+self.countNodes(root.left)+self.countNodes(root.right))
"""
直觉感觉好像最坏情况下是 O(N*logN) 吧，因为之前的 while 需要 logN 的时间，最后要 O(N) 的时间向左右子树递归：
关键点在于，这两个递归只有一个会真的递归下去，另一个一定会触发 hl == hr 而立即返回，不会递归下去。
return int(1+self.countNodes(root.left)+self.countNodes(root.right))
"""