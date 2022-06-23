# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""第一种思路 通过遍历一遍二叉树得到答案

    """


class Solution(object):
    cur_depth = 0
    res = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverse(root):
            if root == None:
                return
            self.cur_depth += 1
            self.res = max(self.cur_depth, self.res)
            traverse(root.left)
            traverse(root.right)
            self.cur_depth -= 1
        traverse(root)
        return self.res


"""
第二种思路，是否可以定义一个递归函数，通过子问题的答案推导出原问题的答案。
如果可以写出这个函数的定义，并充分利用这个函数的返回值
            """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    cur_depth = 0
    res = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 定义：输入根节点，返回这棵二叉树的最大深度
        def traverse(root):
            if root == None:
                return 0
            # 利用定义，计算左右子树的最大深度
            left_depth = traverse(root.left)
            right_depth = traverse(root.right)
            # 整棵树的最大深度等于左右子树的最大深度取最大值，
            # 然后再加上根节点自己
            return max(left_depth, right_depth)+1
        res = traverse(root)
        return res
