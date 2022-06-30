# https://leetcode.cn/problems/moving-average-from-data-stream/
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.capacity = size
        self.current_sum = 0
        self.q = deque()

    def next(self, val: int) -> float:
        if len(self.q) == self.capacity:
            deletedVal = self.q.popleft()
            self.current_sum -= deletedVal
        self.q.append(val)
        self.current_sum += val
        return self.current_sum/len(self.q)
