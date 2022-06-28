# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    rank=0
    res=0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def traverse(root):
            if root == None: return
            traverse(root.left)
            self.rank+=1
            if self.rank==k:
                self.res=root.val
                return root.val
            traverse(root.right)
        traverse(root)
        return self.res