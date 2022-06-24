# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/?show=1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, start, end):
            if start > end:
                return None
            root_val = preorder[start]
            root = TreeNode(root_val)
            p = start+1
            while p <= end and preorder[p] < root_val:
                p += 1
            root.left = build(preorder, start+1, p-1)
            root.right = build(preorder, p, end)
            return root
        return build(preorder, 0, len(preorder)-1)
#
