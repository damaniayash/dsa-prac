# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_length(head:ListNode):
    itr = head
    count = 0
    if head == None:
        return 0
    while itr != None:
        itr = itr.next
        count += 1
    return count

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = get_length(head) - n
        if index == 0:
            head = head.next
        itr = head
        count = 0
        while itr != None:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next   
            count += 1
        return head