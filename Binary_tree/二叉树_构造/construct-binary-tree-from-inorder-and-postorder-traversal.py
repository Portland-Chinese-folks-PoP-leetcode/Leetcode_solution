class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build(inorder, instart, inend, postorder, poststart, postend):
            if instart > inend:
                return None
            rootval = postorder[postend]
            index = inorder.index(rootval)
            leftsize = index-instart
            root = TreeNode(rootval)
            root.left = build(inorder, instart, index-1,
                              postorder, poststart, poststart+leftsize-1)
            root.right = build(inorder, index+1, inend,
                               postorder, poststart+leftsize, postend-1)

            return root

        return build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
