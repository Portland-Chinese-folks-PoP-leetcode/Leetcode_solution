# https://leetcode.cn/problems/implement-queue-using-stacks/
from collections import deque


class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:  # 用 push 让元素入队时，只要把元素压入 s1 即可
        self.s1.append(x)  # 从队尾加入

    def pop(self) -> int:  # 对于 pop 操作，只要操作 s2 就可以了
        self.peek()
        return self.s2.pop()

    """ 
    peek 查看队头的元素怎么办呢？按道理队头元素应该是 1，
    但是在 s1 中 1 被压在栈底，现在就要轮到 s2 起到一个中转的作用了：
    当 s2 为空时，可以把 s1 的所有元素取出再添加进 s2，这时候 s2 中元素就是先进先出顺序了。
    """

    def peek(self) -> int:

        if len(self.s2) == 0:  # 如果s2是空的时候把所有s1中的元素压入s2中
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0


q = MyQueue()
print(q.push(1))
print(q.push(2))
print(q.peek())
