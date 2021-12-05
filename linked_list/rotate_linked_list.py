# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def get_length(head):
    itr = head
    count = 0
    while itr != None:
        itr = itr.next
        count += 1
    return count
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if k == 0:
            return head
        n = get_length(head)
        k = k % n
        if k == 0:
            return head
        init = head
        for i in range(0,n-k-1):
            init = init.next
        nhead = init.next
        init.next = None
        init = nhead
        while init.next != None:
            init = init.next
        init.next = head
        return nhead
        