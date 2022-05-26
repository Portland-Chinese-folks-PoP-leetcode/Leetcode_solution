# https://leetcode.cn/problems/house-robber-ii/submissions/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            n = len(nums)
            dp = [0 for i in range(n+1)]
            dp[1] = nums[0]
            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])

            return dp[-1]
        if len(nums) <= 1:
            return nums[0]
        s1 = dp(nums[1:])
        s2 = dp(nums[:-1])
        return max(s1, s2)
