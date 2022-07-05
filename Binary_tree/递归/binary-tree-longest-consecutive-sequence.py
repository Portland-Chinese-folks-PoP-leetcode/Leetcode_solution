# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    """也是用了外部变量res来记录longest consrcutive sequence
    思考什么时候可以用到这种外部变量，这种外部变量可能是true false 也可能是res。
    碰到那个specific one，到这个就能觉得 整个题目的走向 True or false 或者 longest shortest。可以用外部变量来揭露
    """

    def longestConsecutive(self, root: TreeNode) -> int:
        def traverse(root, parent_val, length):
            if root == None:
                return
            cur_length = length
            if parent_val == None or root.val-parent_val == 1:
                cur_length = cur_length+1
                self.res = max(cur_length, self.res)
            else:  # 我少了这个else的部分
                cur_length = 1
            traverse(root.left, root.val, cur_length)
            traverse(root.right, root.val, cur_length)
        traverse(root, None, 0)
        return self.res
#
