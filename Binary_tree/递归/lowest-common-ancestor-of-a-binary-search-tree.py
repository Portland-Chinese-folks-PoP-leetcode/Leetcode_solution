class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None: return
        if p.val>q.val:
            return self.lowestCommonAncestor(root,q,p)
        if root.val>=p.val and root.val<=q.val:
            return root
        elif root.val>q.val:
            return self.lowestCommonAncestor(root.left,q,p)
        else:
            return self.lowestCommonAncestor(root.right,q,p)
        
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/
