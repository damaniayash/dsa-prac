'''
minheap + dict solution.
Read the below approach first
This approach is also quite similar but instead of searching for the 
minimum element each iteration we instead maintain a minheap for getting the minimum.
Create a counter
Create a heap based on this counter's keys. We want only unique keys
while heap:
    check whether we have the next con secutive groupsize th element
    if note return False.
    when the counter for ith element is zero:
        if the ith element is not at the top of minheap, we cannot form the required groups.
        See neetcode video fpr proper intuition.
    pop from heap
'''
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = {}
        for card in hand:
            counter[card] = 1 + counter.get(card, 0)

        minheap = list(counter.keys())
        heapq.heapify(minheap)

        while minheap:
            smallest = minheap[0]

            for i in range(smallest, smallest + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True
        

'''
n*2 solution.
Here first create a counter from the hand.
We look for the samllest element and then look if we have the consecutive
elements upto groupSize and print the group.
If at any point we are unable to find a consecutive element we can return False
If we reach all the way to the end, we can form the said groups.
So return True
'''
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = Counter(hand)

        while counter:
            smallest = min(counter.keys())
            if counter.get(smallest, None):
                    if counter[smallest] == 1:
                        counter.pop(smallest)
                    else:
                        counter[smallest] -= 1
            group = []
            group.append(smallest)
            for i in range(1, groupSize):
                if counter.get(smallest + i, None):
                    if counter[smallest + i] == 1:
                        counter.pop(smallest + i)
                    else:
                        counter[smallest + i] -= 1
                    group.append(smallest + i)
                else:
                    return False
            print(group)
        return True
                
        # while hand:
        #     smallest = min(hand)
        #     hand.remove(smallest)
        #     group = []
        #     group.append(smallest)
        #     for i in range(1, groupSize):
        #         if smallest + i in hand:
        #             group.append(smallest + i)
        #             hand.remove(smallest + i)
        #         else:
        #             return False
        #     print(group)
        # return True
            


                

        
