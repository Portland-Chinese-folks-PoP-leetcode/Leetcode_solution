from queue import PriorityQueue
import heapq as hq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# a = ListNode(4)
# b = ListNode(6)
# c = ListNode(3)
# q = PriorityQueue()
# q.put((a.val, a))
# q.put((b.val, b))
# q.put((c.val, c))

# # the difference between tuple and set is that

# while not q.empty():
#     next_item = q.get()
#     print(next_item)

a = ListNode(4)
b = ListNode(6)
c = ListNode(3)
list111 = [a, b, c]
item = [(index, l.val) for index, l in enumerate(list111)]
print(item)
hq.heapify(item)
print(hq.heappop(item))
