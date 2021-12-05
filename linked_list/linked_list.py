class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        count = 0
        itr = self.head
        if index<0 or index>=int(self.get_length()):
            return -1
        
        if index == 0:
            return self.head.data
        
        while itr != None:
            if count == index:
                return itr.data
            count = count + 1
            itr = itr.next 

    def addAtHead(self, val: int) -> None:
        temp = Node(val,self.head)                   
        self.head = temp  
        

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val,None)               #Head now points to the first Node
            return
        itr = self.head
        #print((itr.next))
        while itr.next != None:                       #You are at the last element, since iter.next
            itr = itr.next
        itr.next = Node(val,None) 
        
    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr != None:
            count = count+1
            itr = itr.next
        #print("Length is {}".format(count))
        return count    

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>int(self.get_length()):
            return
        if index == 0:
            new = Node(val,self.head)
            self.head = new
        count = 0
        itr = self.head
        while itr != None:
            if count == index - 1:
                new = Node(val,itr.next)
                itr.next = new
                break
            itr = itr.next
            count = count + 1 

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=int(self.get_length()):
            return
        if index == 0:
            self.head = self.head.next                #
        count = 0
        itr = self.head
        while itr != None:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count +1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)