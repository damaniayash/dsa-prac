# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if head.next:
            temp = head.next.next
            node = head
            head = head.next
            head.next = node
            node.next = temp
            self.helper(temp, node)
        return head
    
    def helper(self, head, node):
        if not head:
            return
        if head.next:
            temp = head.next.next
            temp1 = head
            head = head.next
            head.next = temp1
            temp1.next = temp
            node.next = head
            self.helper(temp, temp1)    