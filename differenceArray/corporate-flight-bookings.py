# 这题和 range-addtion 一模一样，这两题都是需要注意一下python的面向对象的编程
# https://leetcode.cn/problems/corporate-flight-bookings/
class difference:
    def __init__(self, nums: List[int]):
        if len(nums) > 0:
            self.diff = [0 for _ in range(len(nums))]
            self.diff[0] = nums[0]
            for i in range(1, len(nums)):
                self.diff[i] = nums[i]-nums[i-1]

    def increment(self, i, j, val):
        self.diff[i] += val
        if j+1 < len(self.diff):
            self.diff[j+1] -= val

    def result(self):
        res = [0 for _ in range(len(self.diff))]
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i-1]+self.diff[i]
        return res


class Solution:

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0 for _ in range(n)]
        df = difference(nums)
        for booking in bookings:
            x = booking[0]-1
            y = booking[1]-1
            val = booking[2]
            df.increment(x, y, val)
        return df.result()
