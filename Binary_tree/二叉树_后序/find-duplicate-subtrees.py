# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        memo={}
        res=[]
        def traverse(root):
            if root == None: return '#'
            left=traverse(root.left)
            right=traverse(root.right)
            subTree= str(left) +','+str(right)+','+str(root.val)
            # print(subTree)
            if subTree not in memo: memo[subTree]=0
            freq=memo[subTree]
            if freq==1: 
                # print('this is root',root)
                res.append(root)
            memo[subTree]=freq+1
            # print(res)
            return subTree
        traverse(root)
        return res
