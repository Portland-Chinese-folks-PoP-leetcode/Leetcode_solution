# bucket perspective
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k > len(nums):
            return False
        sum_number = sum(nums)
        if sum_number % k != 0:
            return False
        used = [False for i in range(0, len(nums))]

        target = sum_number//k

        def backtrack(k, bucket, nums, start, used, target):
            if k == 0:
                return True
            if target == bucket:
                return backtrack(k-1, 0, nums, 0, used, target)
            for i in range(start, len(nums)):
                if used[i]:
                    continue
                if nums[i]+bucket > target:
                    continue
                used[i] = True
                bucket += nums[i]
                if backtrack(k, bucket, nums, i+1, used, target):
                    return True
                used[i] = False
                bucket -= nums[i]
            return False
        return backtrack(k, 0, nums, 0, used, target)
