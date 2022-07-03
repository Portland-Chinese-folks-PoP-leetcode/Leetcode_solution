# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None : return None
        if root==p or root==q: return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left!=None and right!=None: #说明root的left和right正好是p或者q
            return root
        if left==None and right== None: return None # p和q都不在root的 left或者right中
        return right if left==None else left # p和q都在root的 left或者right中