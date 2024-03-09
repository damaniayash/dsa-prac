# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from copy import copy
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other : self.val < other.val

        heap = []

        if not lists:
            return 
        
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        
        if not heap:
            return None

        head_val, head = heapq.heappop(heap)
        if head.next:
            heapq.heappush(heap, (head.next.val, head.next))
        start = head

        while len(heap) > 0:
            val, node = heapq.heappop(heap)
            #print(val, node)
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            head.next = node
            head = node

        return start