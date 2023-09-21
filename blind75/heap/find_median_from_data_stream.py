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