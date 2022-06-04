# https://leetcode.cn/problems/car-pooling/submissions/
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
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0 for _ in range(1000)]
        df = difference(nums)
        for trip in trips:
            # 第 trip[1] 站乘客上车
            val = trip[0]
            # 第 trip[2] 站乘客已经下车，
            #即乘客在车上的区间是 [trip[1], trip[2] - 1]
            i = trip[1]
            j = trip[2]-1
            df.increment(i, j, val)
        res = df.result()
        print(res)
        for i in range(len(res)):
            if capacity < res[i]:
                return False
        return True
