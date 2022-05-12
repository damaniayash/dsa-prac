# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        node = head
        while node.next != None:
            node = node.next
        #print('finally at', node.val)
        if not head.next :
            return head
        temp = head.next
        head.next = None
        fut = temp.next
        temp.next = head
        self.helper(temp, fut)
        
        return node
        
    
    def helper(self, node, fut):
        if not fut:
            return
        temp = fut.next
        fut.next = node
        self.helper(fut, temp)
        
        