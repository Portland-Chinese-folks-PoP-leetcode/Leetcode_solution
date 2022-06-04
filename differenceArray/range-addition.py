#https://leetcode.cn/problems/range-addition/submissions/
class difference:
    # 根据输入的nums 数组 构造出difference array (Construct a difference array based on the input nums array)
    # diff[i]的所记录的定义是 nums[i]比nums[i-1]多了几，少了几。所以说在diff[i]+=val 相当于给nums[i:]后的所有元素都加上了val
    def __init__(self, nums: List[int]):
        if len(nums) > 0:
            self.diff = [0 for _ in range(len(nums))]
            self.diff[0] = nums[0]
            for i in range(1, len(nums)):
                self.diff[i] = nums[i]-nums[i-1]

    def increment(self, i, j, val):
        self.diff[i] += val
        if j+1 < len(self. diff):
            self.diff[j+1] -= val

    def result(self):
        res = [0 for i in range(len(self.diff))]
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i-1]+self.diff[i]
        return res


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0 for _ in range(length)]
        df = difference(nums)
        for update in updates:
            df.increment(update[0], update[1], update[2])
        return df.result()
