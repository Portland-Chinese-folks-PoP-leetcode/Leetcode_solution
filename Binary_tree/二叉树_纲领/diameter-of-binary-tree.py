# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 遇到子树问题，首先想到的是给函数设置返回值，然后在后序位置做文章。
class Solution(object):
    maxdiameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root):
            if root == None:
                return 0
            left_depth = traverse(root.left)
            right_depth = traverse(root.right)
            cur_node_diameter = left_depth+right_depth
            self.maxdiameter = max(self.maxdiameter, cur_node_diameter)
            return max(left_depth, right_depth)+1
        traverse(root)
        return self.maxdiameter
