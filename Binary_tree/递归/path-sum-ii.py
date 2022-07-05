# https://leetcode.cn/problems/path-sum-ii/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(root, targetSum, path):
            if root == None:
                return
            remain = targetSum-root.val
            # 其实这里和 if remain==0 and root.left==None and root.right==None 等价:
            if remain == 0 and root.left == root.right:
                path.append(root.val)
                res.append(list(path))
                path.pop(-1)
                return
            path.append(root.val)
            traverse(root.left, remain, path)  # 对左边进行回溯
            path.pop(-1)

            path.append(root.val)
            traverse(root.right, remain, path)  # 对右边进行回溯
            path.pop(-1)

        res = []
        path = []
        if root == None:
            return res
        traverse(root, targetSum, path)
        return res
