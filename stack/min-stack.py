from collections import deque
# https://leetcode.cn/problems/min-stack/


class MinStack:

    def __init__(self):
        self.stk = deque()
        self.minstk = deque()  # 定义很特别从某元素到栈底的最小元素

    def push(self, val: int) -> None:
        self.stk.append(val)
        # 维护minstack的站定数据，minstack的栈顶数据为全栈的最小元素。
        if len(self.minstk) == 0 or val < self.minstk[-1]:
            self.minstk.append(val)
        else:
            self.minstk.append(self.minstk[-1])

    def pop(self) -> None:
        self.stk.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
