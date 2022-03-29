def canPartition(nums):
    """
        :type nums: List[int]
        :rtype: bool
        """
    s = sum(nums)
    if s % 2 != 0:
        return False
    else:
        n = len(nums)+1
        target = s//2
        dp = [[False for i in range(target+1)] for _ in range(n)]
        for i in range(1, len(nums)+1):
            dp[i][0] = True
        for j in range(1, target+1):
            dp[0][j] = False
        print(dp)

        for i in range(1, n):
            for j in range(1, target+1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    # 这个or用的是相当的巧妙啊 dp[i-1][j-nums[i-1]] 这个请款公司把物品i放入容量为j的背包
                    """
如果不把 nums[i] 算入子集，或者说你不把这第 i 个物品装入背包，那么是否能够恰好装满背包，取决于上一个状态 dp[i-1][j]，继承之前的结果。

如果把 nums[i] 算入子集，或者说你把这第 i 个物品装入了背包，那么是否能够恰好装满背包，取决于状态 dp[i-1][j-nums[i-1]]。

首先，由于 i 是从 1 开始的，而数组索引是从 0 开始的，所以第 i 个物品的重量应该是 nums[i-1]，这一点不要搞混。

dp[i - 1][j-nums[i-1]] 也很好理解：你如果装了第 i 个物品，就要看背包的剩余重量 j - nums[i-1] 限制下是否能够被恰好装满。

换句话说，如果 j - nums[i-1] 的重量可以被恰好装满，那么只要把第 i 个物品装进去，也可恰好装满 j 的重量；否则的话，重量 j 肯定是装不满的。
                    """
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            print('------')
            for i in dp:
                print(i)
        return dp[len(nums)][target]


nums = [1, 5, 11, 5]
print(canPartition(nums))


def print_matrix(list):
    for i in len(list):
        print(i)
