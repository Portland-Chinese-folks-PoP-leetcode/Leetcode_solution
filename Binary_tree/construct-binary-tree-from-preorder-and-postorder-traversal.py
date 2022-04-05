class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build(preorder, prestart, preend, postorder, poststart, postend):
            if prestart > preend:
                return None
            if prestart == preend:
                return TreeNode(preorder[prestart])  # 我的问题是少了这一步
            root_val = preorder[prestart]
            left_postend = preorder[prestart+1]
            index = postorder.index(left_postend)
            leftsize = index-poststart+1
            print(prestart+leftsize)
            root = TreeNode(root_val)
            root.left = build(preorder, prestart+1, prestart +
                              leftsize, postorder, poststart, index)
            root.right = build(preorder, prestart+leftsize+1,
                               preend, postorder, index+1, postend-1)
            return root
        return build(preorder, 0, len(preorder)-1, postorder, 0, len(postorder)-1)




####myun
class my_solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build (preorder,prestart,preend,postorder,poststart,postend):
            if prestart>preend: return None
            if prestart==preend:return TreeNode(preorder[prestart])
            root_val=preorder[prestart]
            left_postend=preorder[prestart+1]
            print(left_postend)
            right_prestart=postorder[postend-1]
            print(right_prestart)
            left_postend_index=postorder.index(left_postend)
            right_prestart_index=preorder.index(right_prestart)
            root=TreeNode(root_val)
            root.left=build(preorder,prestart+1,right_prestart_index-1,postorder,poststart,left_postend_index)
            root.right=build(preorder,right_prestart_index,preend,postorder,left_postend_index+1,postend-1)
            return root
        return build (preorder,0,len(preorder)-1,postorder,0,len(postorder)-1)