"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        itro = head
        while itro != None:
            new = Node(itro.val)
            new.next = itro.next
            itro.next = new
            itro = itro.next.next
        itro = head
        while itro != None:
            if itro.random == None:
                itro.next.random == None
            else:
                itro.next.random = itro.random.next
            itro = itro.next.next
        itro = head
        nhead = itro.next
        itr = nhead
        while itr.next != None:
            itr.next = itr.next.next
            itr = itr.next
        return nhead
        '''
        itro = nhead
        while itro != None:
            print(itro.val)
            itro = itro.next
        '''