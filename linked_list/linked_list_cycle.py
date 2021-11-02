# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # TwoPointer Technique
        fast = head
        slow = head
    
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True    
        return False
        
        '''
        #Hash-Table Technique
        arr = set()
        itr = head
        while itr != None:
            if itr in arr:
                return True
            arr.add(itr)
            itr = itr.next
        return False    
        '''
        
        