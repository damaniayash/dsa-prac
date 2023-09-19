'''
The idea is to create a counter for each of the uniqie task (26 in this case)
push items onto the heap which have the higest frqueuncy.
We need to space these apart so pick them first.
Once an item has been popped from the start we can't push it back until cooldown has expired.
we will keep that item in a queue as a tuple -> (item, time + n)
time + n is the time when we are allowed to poped the item from the queue and insert it into heap.
We will check till for each time step and add item from the queue to the heap if the constion matches.
We require two data structures -> heap and queue.
We have a time counter which increases with each iteration.
Loop will run until either heap or queue has values inside them.

'''
from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = Counter(tasks)
        task_heap, idle_queue = [], deque()
        time = 0
        for k,v in tasks.items():
            task_heap.append((-v, k))
        heapq.heapify(task_heap)
        while task_heap or idle_queue:
            time += 1
            if task_heap:
                count, task = heapq.heappop(task_heap)
                count += 1
                if count != 0:
                    idle_queue.append((count, task, time + n))
            if idle_queue:
                if idle_queue[0][2] == time:
                    count, task, _ = idle_queue.popleft()
                    heapq.heappush(task_heap, (count, task))
        return time

