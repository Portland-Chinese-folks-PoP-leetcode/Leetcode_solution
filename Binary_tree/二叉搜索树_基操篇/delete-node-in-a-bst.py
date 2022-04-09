# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMinNode(root):
            while root.left is not None:
                root = root.left
            return root
        if root == None:
            return None
        if root.val == key:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            minNode = getMinNode(root.right)
            print(minNode)
            root.right = self.deleteNode(root.right, minNode.val)
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root
