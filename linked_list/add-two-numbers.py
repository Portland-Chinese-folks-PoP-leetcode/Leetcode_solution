# https://leetcode.com/problems/add-two-numbers/submissions/
# 本质是用一个节点记录新的节点，在用一个attri 记录新的val。其实是创建了新的一个linkedlist 避免在原有的list上面操作
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        dummy = ListNode(-1)
        p = dummy
        carry = 0  # 记录进位
        while p1 is not None or p2 is not None or carry > 0:
            value = carry
            if p1:
                value += p1.val
                p1 = p1.next
            if p2:
                value += p2.val
                p2 = p2.next
            carry = value//10
            value = value % 10
            p.next = ListNode(value)
            p = p.next
        return dummy.next
