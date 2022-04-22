# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1:ListNode, list2:ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prehead = ListNode(-1)
        prev=prehead
        while list1 and list2:
            if list1.val <=list2.val:
                prev.next=list1
                list1= list1.next
            else:
                prev.next=list2
                list2=list2.next
            prev=prev.next
        prev.next = list1 if list1 is not None else list2
        return prehead.next

if __name__ == '__main__':
    # l1 = [1,2,4]
    l1=ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(4)
    # l2 = [1,3,4]
    l2=ListNode(1)
    l2.next=ListNode(3)
    l2.next.next=ListNode(4)
    a=Solution()
    a.mergeTwoLists(l1,l2)
    