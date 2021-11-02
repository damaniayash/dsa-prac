# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def get_length(head: ListNode):
        if head == None:
            return 0
        count = 0
        itr = head
        while itr != None:
            itr = itr.next
            count = count + 1
        return count

class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        diff = get_length(headA) - get_length(headB)
        print(diff)
        
        itrA = headA
        itrB = headB
        
        if diff < 0:
            for i in range(0,diff * (-1)):
                itrB = itrB.next
        elif diff > 0:
            for i in range(0,diff):
                itrA = itrA.next
                
        while itrA != None:
            if itrA == itrB:
                return itrA
            itrA = itrA.next
            itrB = itrB.next
        return None
        '''
        
        # BruteForce too slow - time limit exceeded
        arr1 = []
        arr2 = []
        itr1 = headA
        itr2 = headB
        while itr1 != None:
            arr1.append(itr1)
            itr1 = itr1.next
        while itr2 != None:
            arr2.append(itr2)
            itr2 = itr2.next
        for i in arr1:
            if i in arr2:
                return i
        return None    
        '''