'''
create two heaps
maxheap -> for the left side of the aray
minheap -> for the right side of the array
We add our num to the maxheap every time.
We want to ensure two things:
1. We want the root of heap heap <= root of minheap. If this is not the case pop from maxheap and push into minheap
2. At anypoint we want our len of heaps to differ by 1. len(maxheap) - len(minheap) < 2.
    If at any point the difference in lengths is greater than 2, we pop the element from bigger heap and push it into smaller heap.   
To find mean:
if sum of len is even.
    return avg of both root.
if odd
    return the root of the heap with bigger length.
'''
import heapq
class MedianFinder:

    def __init__(self):
        self.minheap, self.maxheap = [], []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -1 * num)

        if self.maxheap and self.minheap and (-1 * self.maxheap[0] > self.minheap[0]):
            pop = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, pop)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            pop = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -1 * pop)
        
        if len(self.minheap) > len(self.maxheap) + 1:
            pop = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1 * pop)
        
        # print('maxheap',self.maxheap)
        # print('minheap',self.minheap)
        # print(self.maxheap[0], self.minheap[0])


    def findMedian(self) -> float:
        # print('median call')
        if (len(self.maxheap) + len(self.minheap)) % 2 == 0:
            return ((-1 * self.maxheap[0]) + self.minheap[0]) / 2
        else:
            if len(self.maxheap) > len(self.minheap):
                return -1 * self.maxheap[0]
            else:
                return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


import heapq
class MedianFinder:

    def __init__(self):
        self.length = 0
        self.heap_len = 0
        self.heap = []
        heapq.heapify(self.heap)

    def addNum(self, num: int) -> None:
        self.length += 1
        if self.length == 1:
            self.heap_len = 1
            heapq.heappush(self.heap, num)
            return
        if self.length % 2 == 0:
            self.heap_len += 1
        
        if self.length % 2 == 0:
            heapq.heappush(self.heap, num)
        else:
            heapq.heappushpop(self.heap, num)
        print(self.heap, self.length)

    def findMedian(self) -> float:
        print('heap before median',self.heap, self.length)
        if self.length == 1:
            median = self.heap[0]
            print('median', median)
            return median

        elif self.length == 2:
            median = (self.heap[0] + self.heap[1]) / 2
            print('median', median)
            return median

        elif len(self.heap) == 3 and self.length == 4:
            median = self.heap[0]
            print('median', median)
            return median

        if self.length % 2 == 0:
            median = (self.heap[0] + min(self.heap[1], self.heap[2])) / 2
        else:
            median = self.heap[0]
        print('median', median)
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()