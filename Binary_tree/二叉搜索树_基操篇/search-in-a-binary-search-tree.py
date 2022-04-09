# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)

# 以下是我做的第二个版本

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    res = None

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search(root, val):
            if root == None:
                return
            if root.val == val:
                print(root.val)
                self.res = root
                return root
            if root.val < val:
                return search(root.right, val)
            if root.val > val:
                return search(root.left, val)
        result = search(root, val)
        print(result)
        print(self.res)
        return self.res
