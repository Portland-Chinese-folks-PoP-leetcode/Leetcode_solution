# dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
# longest increasing subsequence
def LIS(nums):
    dp = [1]*(len(nums))
    for i in range(0, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    res = max(dp)
    return res


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(LIS(nums))

# 第二次做 my solution


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        dp = [1 for i in range(len(nums))]  # dp[i]定义 以dp[i]为结尾的子序列最长的子序列
        for i in range(1, len(dp)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        # print(dp)
        return max(dp)
