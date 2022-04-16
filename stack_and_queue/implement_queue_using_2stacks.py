from collections import deque
class MyQueue:

    def __init__(self):
        self.stack1 = deque([])
        self.stack2 = deque([])

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ans = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ans 

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ans = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ans

    def empty(self) -> bool:
        if self.stack1: return False
        else: return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()