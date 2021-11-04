# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
def remove_at_index(head,index):
    if index == 0:
        head = head.next
    itr=head
    count = 0
    while itr != None:
        if count == index - 1:
            itr.next = itr.next.next
            break
        count += 1
        itr = itr.next
    return head
    
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        itr = head
        count = 0
        indexes = []
        while itr != None:
            if itr.val == val:
                indexes.append(count)
            itr = itr.next
            count = count + 1
        count=0
        for i in range(len(indexes)):
            head = remove_at_index(head,indexes[i]-count)
            count=count+1
        return head
            
            
        
                
        
        