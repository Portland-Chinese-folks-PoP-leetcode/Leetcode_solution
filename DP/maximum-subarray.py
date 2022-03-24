def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    状态是什么？
    dp数组的定义：这个dp数组，每个元素的定义是，到在最大的max subarray
    """

    dp = [-100000000]*(len(nums))

    dp[0] = nums[0]

    for i in range(1, len(dp)):
        if nums[i] < dp[i-1]+nums[i]:
            dp[i] = dp[i-1]+nums[i]
        else:
            dp[i] = nums[i]

    return max(dp)

# https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/

# 这个解释解释的很好
#


nums = [5, 15, -30, 10, -5, 40, 10]
print(maxSubArray(nums))
