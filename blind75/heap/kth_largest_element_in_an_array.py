'''
Use minheap.
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        return heap[0]