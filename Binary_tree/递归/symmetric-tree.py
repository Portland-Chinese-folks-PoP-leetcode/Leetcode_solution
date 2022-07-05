# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(A, B):
            if A is None or B is None:
                return A == B  # 俩根节点要相同
            if A.val != B.val:
                return False
            return check(A.left, B.right) and check(A.right, B.left)
        if root == None:
            return True
        return check(root.left, root.right)

### 第二遍我自己的做法，和https://leetcode.cn/problems/same-tree/很相似
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(rootA,rootB):
            if rootA==None and rootB==None:
                return True
            if rootA is None or rootB is None:
                return False
            if rootA.val!=rootB.val: return False
            return check(rootA.left,rootB.right) and check(rootA.right,rootB.left)
            # if A is None or B is None: return A==B # 俩根节点要相同
            # if A.val!=B.val: return False
            # return check(A.left,B.right) and check(A.right,B.left)
        if root==None: return True
        return check(root.left,root.right)