# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def get_length(head):
    count = 0
    if head == None:
        return count
    itr = head
    while itr != None:
        count += 1
        itr = itr.next
    return count
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        even = False
        if get_length(head) % 2 == 0:
            even = True
        rev_index = math.ceil(get_length(head)/2)
        count = 0
        itr = head
        while itr != None:
            if count == rev_index:
                break
            itr = itr.next
            count += 1
        rev = itr
        prev = None
        while rev != None:
            next = rev.next
            rev.next = prev
            prev = rev
            rev = next
        rev = prev
        s1=[]
        while rev!=None:
            s1.append(rev.val)
            rev = rev.next
        #print(s1)
        count = 0
        s2=[]
        itr=head
        
        #print(rev_index)
        if even == False:
            rev_index = rev_index - 1
        #print(rev_index)
        while itr != None:
            if count == rev_index:
                break
            s2.append(itr.val)
            itr = itr.next
            count += 1
        #print(s2)
        if s1 == s2:
            return True
        else:
            return False
        '''  
        rev_index = math.floor(get_length(head)/2)
        count = 0
        itr = head
        print("rev:",rev.val)
        print("itr:",itr.val)
        print("---",rev_index,count)
        while itr != None:
            if rev.val != itr.val:
                print("rev:",rev.val)
                print("itr:",itr.val)
                return False
            if count == rev_index:
                break
            itr = itr.next
            rev = rev.next
            count += 1
        return True
        #print(itr.val)
        
        while rev!=None and itr!= None:
            if rev.val != itr.val:
                return False
            rev = rev.next
            itr = itr.next
        '''
            