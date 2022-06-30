from collections import deque

# https: // leetcode.cn/problems/implement-stack-using-queues/


class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_element = None

    def push(self, x: int) -> None:  # 先说 push API，直接将元素加入队列，同时记录队尾元素，因为队尾元素相当于栈顶元素，如果要 top 查看栈顶元素的话可以直接返回：
        self.q.append(x)
        self.top_element = x

    def pop(self) -> int:  # 底层数据结构是先进先出的队列，每次 pop 只能从队头取元素；但是栈是后进先出，也就是说 pop API 要从队尾取元素.解决方法简单粗暴，把队列前面的都取出来再加入队尾，让之前的队尾元素排到队头，这样就可以取出了.原来的队尾元素被提到队头并删除了，但是 top_elem 变量没有更新.等到在新的队尾元素到对头的时候停止while循环，赋值新的top_element。然后再继续append
        size = len(self.q)
        while size > 2:
            self.q.append(self.q.popleft())
            size -= 1
        self.top_element = self.q[0]
        self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
