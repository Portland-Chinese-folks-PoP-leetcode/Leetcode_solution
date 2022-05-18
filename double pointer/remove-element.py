# https://leetcode.cn/problems/remove-element/submissions/

class Solution:
    def removeElement(self, nums, val: int) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(nums)
        return slow


nums = [0, 1, 4, 0, 2]
val = 0
solution = Solution()

print(solution.removeElement(nums, val))
