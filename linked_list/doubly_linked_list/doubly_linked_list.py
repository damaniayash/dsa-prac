class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def get_length(self):
        if self.head == None:
            return 0
        count = 0
        itr = self.head
        while itr != None:
            count += 1
            itr = itr.next
        return count
    
    def get(self, index: int) -> int:
        count = 0
        itr = self.head
        while itr != None:
            if index == count:
                return itr.data
            itr = itr.next
            count = count + 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        temp = Node(val, self.head,prev = None)
        if self.head == None:
            self.head = temp
            return
        self.head.prev = temp
        self.head = temp
        

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, None, None)
            return
        itr = self.head
        while itr.next != None:
            itr = itr.next
        temp = Node(val,None,itr)
        itr.next = temp
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.get_length():
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == int(self.get_length()):
            self.addAtTail(val)
            return
        itr = self.head
        count = 0
        while itr != None:
            if count == index - 1:
                temp = Node(val,itr.next,itr)
                itr.next = temp
                temp.prev = itr
                temp.next.prev = temp
            itr = itr.next
            count = count + 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.get_length():
            return
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            #self.head.prev = None   
            return
        count = 0
        itr = self.head
        while itr != None:
            if count == index - 1:
                if itr.next.next == None:
                    itr.next = None
                    break
                itr.next.next.prev = itr
                itr.next = itr.next.next
                break  
            itr = itr.next
            count += 1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

'''
class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert_front(self,data):
        temp = Node(data, self.head,prev = None)
        if self.head == None:
            self.head = temp
            return
        self.head.prev = temp
        self.head = temp

    def insert_end(self,data):
        if self.head == None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next != None:
            itr = itr.next
        temp = Node(data,None,itr)
        itr.next = temp
    
    def insert_index(self,data,index):
        if index == 0:
            self.insert_front(data)
            return
        if index == int(self.get_length()):
            self.insert_end(data)
            return
        itr = self.head
        count = 0
        while itr != None:
            if count == index - 1:
                temp = Node(data,itr.next,itr)
                itr.next = temp
                temp.prev = itr
                temp.next.prev = temp
            itr = itr.next
            count = count + 1
    
    def get_length(self):
        if self.head == None:
            return 0
        count = 0
        itr = self.head
        while itr != None:
            count += 1
            itr = itr.next
        return count
    
    def delete_index(self,index):
        if index<0 or index >= int(self.get_length()):
            return
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            #self.head.prev = None   
        count = 0
        itr = self.head
        while itr != None:
            if count == index - 1:
                if itr.next.next == None:
                    itr.next = None
                    break
                itr.next.next.prev = itr
                itr.next = itr.next.next
                break  
            itr = itr.next
            count += 1
             
    def print(self):
        if self.head == None:
            return
        itr = self.head
        llstr = ''
        while itr != None:
            llstr = llstr + str(itr.data) + ' ==> '
            itr = itr.next
        return llstr
    
    def get(self,index):
        count = 0
        itr = self.head
        while itr != None:
            if index == count:
                return itr.data
            itr = itr.next
            count = count + 1
        return -1


    
    def reverse(self):
        itr = self.head
        rev = ''
        while itr.next != None:
            itr = itr.next
        print(itr.data)
        while itr != None:
            rev = rev + str(itr.data) + ' ==> '
            itr = itr.prev
        print(rev)


ll = Linked_list()
ll.insert_front(2)
print(ll.print())
ll.delete_index(1)
ll.insert_front(2)
ll.insert_front(3)
ll.insert_front(2)
ll.insert_front(5)
ll.insert_front(5)
ll.insert_end(5)
print(ll.print())
ll.delete_index(6)
ll.delete_index(4)


ll.insert_front(12)
print(ll.print())
ll.insert_front(123)
print(ll.print())

print('reached')
ll.insert_end(23)
print(ll.print())
ll.insert_end(34)
print(ll.print())

ll.insert_index(100,2)
print(ll.print())
ll.delete_index(4)
print(ll.print())
ll.reverse()
print(ll.print())
print(ll.get(7))

ll.delete_index(4)
print(ll.print())
ll.reverse()
'''
