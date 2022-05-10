# https://leetcode.cn/problems/merge-k-sorted-lists/submissions/
#
#
import heapq
from Queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p = dummy
        pq = PriorityQueue()
        for head in lists:
            if head is not None:
                pq.put((head.val, head))
        while not pq.empty():
            val, node = pq.get()
            p.next = node
            p = p.next
            node = node.next
            if node:
                pq.put((node.val, node))
        return dummy.next


# heapq version
# https://leetcode.cn/problems/merge-k-sorted-lists/submissions/
#


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(-1)
        p = dummy
        hq = []
        for idx, i in enumerate(lists):
            if i:
                heapq.heappush(hq, (i.val, idx))

        while hq:
            cur, idx = heapq.heappop(hq)
            p.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx] is not None:
                heapq.heappush(hq, (lists[idx].val, idx))
            p = p.next
        return dummy.next
