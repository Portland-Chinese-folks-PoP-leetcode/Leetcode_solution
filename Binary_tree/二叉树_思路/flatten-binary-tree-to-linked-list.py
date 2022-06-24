# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        # 利用定义，把左右子树拉平
        self.flatten(root.left)
        self.flatten(root.right)
        # /**** 后序遍历位置 ** **/
        # 1、左右子树已经被拉平成一条链表
        left_node = root.left
        right_node = root.right
        # 2、将左子树作为右子树
        root.left = None
        root.right = left_node
        # 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right_node


""" 思路
# 输入节点 root，然后 root 为根的二叉树就会被拉平为一条链表
# 1、先利用 flatten(x.left) 和 flatten(x.right) 将 x 的左右子树拉平。
# 2、将 x 的右子树接到左子树下方，然后将整个左子树作为右子树。
"""
