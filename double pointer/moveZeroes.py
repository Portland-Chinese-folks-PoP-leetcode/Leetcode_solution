#https://leetcode.cn/problems/move-zeroes/submissions/
# 这道题的前面还是使用了 removeElement
# 题目让我们将所有 0 移到最后，其实就相当于移除 nums 中的所有 0，然后再把后面的元素都赋值为 0 即可
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0: return 0
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        for i in range(slow,len(nums)):
            nums[i]=0
        return nums
    