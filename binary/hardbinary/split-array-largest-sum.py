class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def f(nums, x):
            days = 0
            cap = x
            i = 0
            while i < len(nums):
                cap = x
                while i < len(nums):
                    if cap < nums[i]:
                        break
                    else:
                        cap -= nums[i]
                    i += 1
                days += 1
            return days
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = left+(right-left)//2
            if f(nums, mid) == m:
                right = mid-1
            elif f(nums, mid) < m:
                right = mid-1
            elif f(nums, mid) > m:
                left = mid+1
        return left
