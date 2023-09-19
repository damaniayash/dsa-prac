'''
This is basically kth largest element but k = len(nums)-k+1
However this problem is supposed to be solved using binary search.
The idea is that we keep track of how many items to the left of mid are smaller or equal to the current mid.
When count == k, we would have reached the kth smallest element.
'''
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = list(chain.from_iterable(matrix))
        k = len(nums) - k + 1
        num_heap = []
        heapq.heapify(num_heap)
        for num in nums:
            if len(num_heap) == k:
                heapq.heappushpop(num_heap, num)
            else:
                heapq.heappush(num_heap, num)
        return num_heap[0]