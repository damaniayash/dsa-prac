
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
        if abs(self.head - self.tail) == self.length - 1:
            return True
        elif self.head > self.tail and abs(self.head - self.tail) == 1:
            return True
        return False
        
que = circular_queue(5)
print(que.queue)
print('head',que.head,'tail',que.tail)
que.enQueue(5)
que.enQueue(13)
que.enQueue(8)
que.enQueue(2)
que.enQueue(10)
print('head',que.head,'tail',que.tail)
print(que.queue)
print(que.Front())
print(que.Rear())
que.deQueue()
print('head',que.head,'tail',que.tail)
print(que.queue)
que.deQueue()
print('head',que.head,'tail',que.tail)
print(que.queue)
que.enQueue(23)
print('head',que.head,'tail',que.tail)
print(que.queue)
que.enQueue(6)
print('head',que.head,'tail',que.tail)
print(que.queue)
que.deQueue()
print('head',que.head,'tail',que.tail)
print(que.queue)
que.deQueue()
print('head',que.head,'tail',que.tail)
print(que.queue)
que.deQueue()
print('head',que.head,'tail',que.tail)
print(que.queue)
que.deQueue()
print('head',que.head,'tail',que.tail)
print(que.queue)
que.deQueue()
print('head',que.head,'tail',que.tail)
print(que.queue)
print(que.Front())
print(que.Rear())