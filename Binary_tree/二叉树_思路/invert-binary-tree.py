# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 「分解问题」的思维模式
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

    """遍历的思维模式"""

    def invertTree_v2(self, root) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(root):
            if root == None:
                return

            traverse(root.left)
            traverse(root.right)
            tmp = root.left
            root.left = root.right
            root.right = tmp
            traverse(root)
            return root
