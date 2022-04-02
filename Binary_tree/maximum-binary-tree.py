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
        def build(nums):
            # if low > high:
            #     return None
            if len(nums) == 0:
                return None
            # 这是使用了前序
            max_val = max(nums)
            index = nums.index(max_val)
            root = TreeNode(max_val)

            root.left = build(nums[0:index])
            root.right = build(nums[index+1:])
            return root

        return build(nums)
