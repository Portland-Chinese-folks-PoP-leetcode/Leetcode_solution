class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [0 for i in range(0, len(nums)+1)]
        for i in range(1, len(nums)+1):
            self.presum[i] = self.presum[i-1]+nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1]-self.presum[left]
