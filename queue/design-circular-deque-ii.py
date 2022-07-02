# 641  https://leetcode.cn/problems/design-circular-deque/

from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.double_q = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.double_q) == self.capacity:
            return False
        self.double_q.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.double_q) == self.capacity:
            return False
        self.double_q.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.double_q) == 0:
            return False
        self.double_q.popleft()
        return True

    def deleteLast(self) -> bool:
        if len(self.double_q) == 0:
            return False
        self.double_q.pop()
        return True

    def getFront(self) -> int:
        if len(self.double_q) == 0:
            return -1
        return self.double_q[0]

    def getRear(self) -> int:
        if len(self.double_q) == 0:
            return -1
        return self.double_q[-1]

    def isEmpty(self) -> bool:
        return len(self.double_q) == 0

    def isFull(self) -> bool:
        return len(self.double_q) == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
