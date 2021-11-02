class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        arr = []
        itr = head
        while itr != None:
            if itr in arr:
                return arr[-1].next
            arr.append(itr)
            itr = itr.next
        return None