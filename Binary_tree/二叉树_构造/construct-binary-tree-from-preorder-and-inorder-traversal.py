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
            index = inorder.index(root_val)
            left_size = index-instart
            root = TreeNode(root_val)
            print(preorder)
            print(root)
            root.left = build(preorder, prestart+1, prestart +
                              left_size, inorder, instart, index-1)
            root.right = build(preorder, prestart+left_size+1,
                               preend, inorder, index+1, inend)
        return build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
