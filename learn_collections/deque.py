from collections import deque
d = deque()
d.append('a')
d.append('b')
d.appendleft('x')
print(d)
d.popleft()
d.pop()
print(d)
