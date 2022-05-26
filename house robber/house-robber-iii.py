# https://leetcode.cn/problems/house-robber-iii/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}

        def dp(root):
            if root == None:
                return 0
            if root in memo:
                return memo[root]
            # 抢一波
            do_it = root.val+(0 if root.left == None else dp(root.left.left)+dp(root.left.right))+(
                0 if root.right == None else dp(root.right.left)+dp(root.right.right))
            # 不抢
            not_do = dp(root.left)+dp(root.right)
            res = max(do_it, not_do)
            memo[root] = res
            return res
        return dp(root)
