from heapq import heapify, heappop, heappush
'''
Using heap
Make the heap from the stones array, first multiply array by -1 since python heaps are minheaps.
Pop the two heaviest stones and push the abs of the weight different.
Continue this until len(stones) > 1.
return the single element left in the array
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            num1 = abs(heappop(stones))
            num2 = abs(heappop(stones))
            heappush(stones, -1 * abs(num1 - num2))
        return abs(stones[0])
'''
This is the brute force solution.
Sort the array first. 
Iterate from end to start:
    sort the array every time (yikes, but the arrays are almost sorted so timsort takes less time)
    add the difference to the second last element and pop the last element

This might seem slow but it is actually faster than using heap.
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)-1, 0, -1):
            stones = sorted(stones)
            stones[i-1] = abs(stones[i] - stones[i-1])
            stones.pop()
        return stones[0]