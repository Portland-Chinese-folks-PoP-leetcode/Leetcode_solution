def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [-100000000]*(len(nums))

    dp[0] = nums[0]

    for i in range(1, len(dp)):

        dp[i] = max(nums[i], dp[i-1]+nums[i])

    return max(dp)

# https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/

# 这个解释解释的很好
#
