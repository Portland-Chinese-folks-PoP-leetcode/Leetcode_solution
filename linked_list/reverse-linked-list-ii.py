# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        def reverseN(head, n):
            if n == 1:
                return head
            # 以 head.next 为起点，需要反转前 n - 1 个节点
            last = reverseN(head.next, n-1)
            successor = head.next.next
            # 以head.next为开头的链表已经完成翻转，那么head.next.next正确指向后继节点
            head.next.next = head
            head.next = successor
            return last
        if m == 1:
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

# 第二个版本 我个人更喜欢第二个版本
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # 函数的定义是返回
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # reverseN 的定义是 翻转前N个node并返回头结点
        def reverseN(head, n):
            if n == 1:
                successor = head.next
                return head, successor
            last, successor = reverseN(head.next, n-1)
            head.next.next = head
            head.next = successor
            return last, successor

        if left == 1:
            res, _ = reverseN(head, right)
            return res
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head
