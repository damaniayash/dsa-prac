
class circular_queue:
    def __init__(self, k: int):
        self.length = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull() == False:
            if self.head == -1 and self.tail == -1:
                self.head = 0
                self.tail = 0
                self.queue[self.tail] = value
                return True
            else:
                print("entered else")
                self.tail = (self.tail + 1) % self.length 
                self.queue[self.tail] = value
                return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.isEmpty() == False:
            if self.head == self.tail:
                self.head, self.tail = -1, -1
                self.queue = [None] * self.length
                return True
            else:
                self.queue[self.head] = None
                self.head = (self.head + 1) % self.length
                return True
        else:
            return False


    def Front(self) -> int:
        if self.isEmpty() == False:
            return self.queue[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if self.isEmpty() == False:
            return self.queue[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.head == -1 and self.tail == -1:
            return True
        return False

    def isFull(self) -> bool:
        if None not in self.queue:
            return True
        else: 
            return False
        # if abs(self.head - self.tail) == self.length - 1 and None not in:
        #     print('full ho gaya')
        #     return True
        # elif self.head > self.tail and abs(self.head - self.tail) == 1:
        #     return True
        # return False
        
que = circular_queue(3)
print(que.queue)
print('head',que.head,'tail',que.tail)
que.enQueue(1)
que.enQueue(2)
que.enQueue(3)
print('head',que.head,'tail',que.tail)
print(que.queue)
que.deQueue()
print('head',que.head,'tail',que.tail)
print(que.queue)
que.deQueue()
print('head',que.head,'tail',que.tail)
print(que.queue)
print(que.enQueue(3))
print('head',que.head,'tail',que.tail)
print(que.queue)
print(que.enQueue(5))
print('head',que.head,'tail',que.tail)
print(que.queue)

# def isFull(self) -> bool:
#     if abs(self.head - self.tail) == self.length - 1 and None not in:
#         print('full ho gaya')
#         return True
#     elif self.head > self.tail and abs(self.head - self.tail) == 1:
#         return True
#     return False
# test_from_work_laptop