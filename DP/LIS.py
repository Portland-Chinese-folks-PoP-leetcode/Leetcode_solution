#dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
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
