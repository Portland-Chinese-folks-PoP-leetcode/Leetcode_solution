
# Nsum的问题在于如何熟练使用 hash表
# This is my solution
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable:
                return [hashtable[nums[i]], i]
            hashtable[target-nums[i]] = i
# labuladong solution


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        index = {}
        for i in range(n):
            index[nums[i]] = i
        for i in range(n):
            other = target-nums[i]
            if other in index and index[other] != i:
                return[i, index[other]]
        return [-1, -1]
