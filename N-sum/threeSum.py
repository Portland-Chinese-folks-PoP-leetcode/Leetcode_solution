class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def nSumTarget(nums, n, start, target):
            sz = len(nums)
            res = []
            if n < 2 or sz < n:
                return res  # It has to be at least 2 sum and the length of nums should not less than n
            if n == 2:  # This is the base case
                lo, hi = start, sz-1
                while lo < hi:
                    sum1 = nums[lo]+nums[hi]
                    left, right = nums[lo], nums[hi]
                    if sum1 < target:
                        while lo < hi and nums[lo] == left:
                            lo += 1
                    elif sum1 > target:
                        while lo < hi and nums[hi] == right:
                            hi -= 1
                    else:
                        res.append([left, right])
                        while lo < hi and nums[lo] == left:
                            lo += 1
                        while lo < hi and nums[hi] == right:
                            hi -= 1
            else:
                # n > 2 时，递归计算 (n-1)Sum 的结果
                for i in range(start, sz):
                    sub = nSumTarget(nums, n-1, i+1, target-nums[i])
                    for arr in sub:
                        # (n-1)Sum 加上 nums[i] 就是 nSum
                        arr.append(nums[i])
                        if arr not in res:
                            res.append(arr)
                    while i < sz-1 and nums[i] == nums[i+1]:
                        i += 1
            return res

        nums = sorted(nums)
        result = nSumTarget(nums, 3, 0, 0)
        return result
