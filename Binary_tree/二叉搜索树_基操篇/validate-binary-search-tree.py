# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
根据 BST 的定义，root 的整个左子树都要小于 root.val，整个右子树都要大于 root.val。
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValidBSTTraverse(root,min,max):
            if root == None: return True
            if min!=None and root.val<=min: return False
            if max!=None and root.val>=max: return False
            return isValidBSTTraverse(root.left,min,root.val) and isValidBSTTraverse(root.right,root.val,max)
        return isValidBSTTraverse(root,None,None)
    
