from collections import OrderedDict
import collections
a = OrderedDict()
print(dir(a))


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(-1)

a = ListNode(1)
head.next = a
b = ListNode(2)
a.next = b
c = ListNode(3)
b.next = c
d = ListNode(2)
c.next = d
e = ListNode(1)
d.next = e

global left
left = head


def traverse_pre(head):
    global left
    if head is None:
        return

    traverse_pre(head.next)
    print('PRE ORDER', left.val)
    left = left.next
    print(head.val)


traverse_pre(head)


def removeDuplicates(nums):
    fast, slow = 0, 0
    memo = dict()
    while fast < len(nums):
        if nums[fast] not in memo:
            memo[nums[fast]] = 1
        else:
            memo[nums[fast]] += 1

        if nums[fast] != nums[slow] or memo[nums[fast]] <= 2:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


nums = [0, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4]
removeDuplicates(nums)
