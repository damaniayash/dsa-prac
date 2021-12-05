# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        carry = 0
        while l1 != None or l2 != None:
            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next
            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next
            sum12 = val1 + val2 + carry
            unit = sum12 % 10
            carry = sum12 // 10
            #print(sum12,unit,carry)
            new = ListNode()
            new.val = unit
            if head == None:
                head = new
                itr = head
            else:
                itr.next = new
                itr = new
        itr = head
        if carry == 1:
            new = ListNode()
            new.val = 1
            while itr.next != None:
                itr = itr.next
            #print(f"reached : {itr.val}")
            itr.next = new
        return head
        
            
            
                
            
            