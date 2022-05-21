# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/submissions/
# 左右双指针

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            result = numbers[left]+numbers[right]
            if result == target:
                return[left+1, right+1]
            elif result < target:
                left += 1
            elif result > target:
                right -= 1
        return [-1, -1]
