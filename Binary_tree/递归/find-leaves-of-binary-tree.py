# https://leetcode.cn/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """这是我的解法
    """

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def traverse(root, parent, flag):
            if root == None:
                return
            if root.left is None and root.right is None:
                level.append(root.val)
                if flag == 'left':
                    parent.left = None
                if flag == 'right':
                    parent.right = None
            traverse(root.left, root, 'left')
            traverse(root.right, root, 'right')
        res = []
        while root.left or root.right:
            level = []
            traverse(root, None, None)
            res.append(level)
        res.append([root.val])
        return res

# labuladong
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    res = []

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def traverse(root):
            if root == None:
                return 0
            # 当前节点距离叶子节点的高度（最大深度）
            h = max(traverse(root.left), traverse(root.right))+1
            if len(res) < h:
                res.append([])
            # 把所有相同高度的叶子节点放在一起
            res[h-1].append(root.val)
            return h
        res = []
        traverse(root)
        return res
