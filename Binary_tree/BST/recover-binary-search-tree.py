# 这是我的解法 https://leetcode.cn/problems/recover-binary-search-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre_val = float('-inf')
        res = []
        root_res = []
        stack = deque()
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # pre_val=root.val if root.val>pre_val
            res.append(root.val)
            root_res.append(root)
            root = root.right
        res = sorted(res)
        print(res)
        for i in range(len(root_res)):
            root_res[i].val = res[i]

# 思路，
# 1 用一遍的BST的中序遍历获得两个list 一个存储root.val一个存储 root。
# 2 sorted一下存储 root.val的数组
# 3把 sorted过后 root.val的数组 一个一个赋值给 存储 root的数组
# 相当于是时间换空间
