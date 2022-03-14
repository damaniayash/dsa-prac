
class circular_queue:
    def __init__(self, k: int):
        self.length = k
        self.queue = []
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull() == False:
            if self.head == -1 and self.tail == -1:
                self.head = 0
                self.tail = 0
                print(self.tail)
                self.queue.append(value)
                return True
            else:
                print("entered else")
                self.tail = self.tail % self.length + 1
                self.queue.append(value)
                return True
        else:
            print('queue is full')

    def deQueue(self) -> bool:
        

    def Front(self) -> int:
        pass

    def Rear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
        if abs(self.head - self.tail) == self.length - 1:
            return True
        elif self.head > self.tail and abs(self.head - self.tail) == 1:
            return True
        return False
        
que = circular_queue(5)
print(que.queue)
print('head',que.head,'tail',que.tail)
que.enQueue(1)
que.enQueue(2)
que.enQueue(3)
que.enQueue(4)
que.enQueue(5)
que.enQueue(6)

print(que.queue)
