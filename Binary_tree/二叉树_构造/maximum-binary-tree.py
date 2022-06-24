# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build(nums, lo, hi):
            if lo > hi:
                return None
            root_val = max(nums[lo:hi+1])
            index = nums.index(root_val)
            root = TreeNode(root_val)
            root.left = build(nums, lo, index-1)
            root.right = build(nums, index+1, hi)
            return root
        return build(nums, 0, len(nums)-1)


"""当前 nums 中的最大值就是根节点，然后根据索引递归调用左右数组构造左右子树即可。
"""

# 第二次解法


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(
            nums[:nums.index(max(nums))])
        root.right = self.constructMaximumBinaryTree(
            nums[nums.index(max(nums))+1:])

        return root
