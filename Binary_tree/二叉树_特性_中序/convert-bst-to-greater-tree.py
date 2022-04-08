# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def traverse(root):
            if root == None:
                return 0
            right_sum = traverse(root.right)
            self.res = self.res+root.val
            root.val = self.res
            # print('current root is',root.val)
            left_sum = traverse(root.left)

            # current=root.val+left_sum+right_sum

        traverse(root)
        return root
