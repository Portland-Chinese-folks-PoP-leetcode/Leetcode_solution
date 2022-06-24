# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(preorder, prestart, preend, inorder, instart, inend):
            if prestart > preend:
                return None
            root_val = preorder[prestart]
            root = TreeNode(root_val)
            index = inorder.index(root_val)
            left_size = index-instart
            root.left = build(preorder, prestart+1, prestart +
                              left_size, inorder, instart, index-1)
            root.right = build(preorder, prestart+left_size+1,
                               preend, inorder, index+1, inend)
            return root
        return build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
