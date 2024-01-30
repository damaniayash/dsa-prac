'''
First solution.
traverse the array twice and see if we can reach the same index again
Maintain a visted set and add the reachable indexes.
If an index can't be reached reset tank and visited set to 0
otherwise add index to set
if we find the same index again return the index.
If we reach the end of the 2x array this means it is impossible to complete a round trip.
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        visited = set()
        start = True
        gas, cost = gas + gas, cost + cost
        
        for i in range(0, len(gas)):

            i = i % (len(gas)//2) 

            if i in visited:
                return i

            if start:
                tank = tank + gas[i]
            else:
                tank = tank + gas[i] - cost[i-1]

            if cost[i] > tank:
                visited = set()
                tank = 0
                start = True
            else:
                visited.add(i)
                start = False

        return -1
            