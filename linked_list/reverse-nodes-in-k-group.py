# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(a, b):
            pre = None
            cur = a
            nxt = a
            while cur != b:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        if head == None:
            return None
        # 区间 [a, b) 包含 k 个待反转元素
        a = head
        b = head
        for i in range(k):
            # 当前linked list不足k个元素，不需要反转，
            if b == None:
                return head
            b = b.next
        # 反转前 k 个元素
        newHead = reverse(a, b)  # 这个newhead其实就是b
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return newHead
