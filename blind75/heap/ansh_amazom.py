import heapq
def min_cost(a, b, m):
    pq = []
    for j in range(1, len(a)):
        for i in range(len(a)):
            heapq.heappush(pq, a[i] + (j-1)*b[i])

    return sum(heapq.nsmallest(m, pq))

from heapq import heapify, heapreplace

def getMinimumCost(a, b, m):
    priceheap = list(zip(a, b))  # (price, increase) tuples
    heapify(priceheap)  # from now on its a minheap

    minimum_cost = 0
    for _ in range(m):
        price, increase = priceheap[0]  # cheapest
        # increase price of the selected item for next time:
        heapreplace(priceheap, (price + increase, increase))
        minimum_cost += price

    return minimum_cost

a = [1,3,2]
b = [2,1,3]
m = 5
print(getMinimumCost(a, b, m))