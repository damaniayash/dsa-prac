'''
Idea is to use max heap to store the k closest element.
We push (-ve distance, point) onto the heap. Python will take the first element in the tuple as key for heap comparisison.
Since we push -ve distance, the maximum distance (smallest from heap perspective) will be top.
Every time we pop from the heap the point with max distance from origin popped.
We push points onto the heap until the len(heap) is less than k.
When the len(heap) == k. We have the smallest possible points up until that point.
This is beacuse we popped the max distance at each pop.
When the len(heap) == k. For every new point we push the point but also pop a point.
We can the len(heap) == k so heappushpop is called.
'''

import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            distance = -1 * math.sqrt(point[0]**2 + point[1]**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (distance, point))
            else:
                heapq.heappush(heap, (distance, point))
        return [x[1] for x in heap]


import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            distance = -1 * math.sqrt(point[0]**2 + point[1]**2)
            if len(heap) == k:
                if heap[0][0] > distance:
                    continue
                heapq.heappop(heap)
            heapq.heappush(heap, (distance, point))
        ans = [x[1] for x in heap]
        return ans
