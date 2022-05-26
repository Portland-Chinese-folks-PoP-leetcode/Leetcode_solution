# https://leetcode.cn/problems/house-robber/submissions/
# 这是我的做法
class Solution1:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums)+1)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return max(dp[-1], dp[-2])

# 这是labuladong的dp解法


class Solution2:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n+1)]
        dp[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2]+nums[i])

        return dp[0]
