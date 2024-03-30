'''
Same as course schedule but return the entire topsort instead of True/False.
Find topological sort using Kahn's algorithm.
'''
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i:[] for i in range(numCourses)}
        in_degree = {i:0 for i in range(numCourses)}
        queue = deque()
        topsort = []

        for child, parent in prerequisites:
            graph[parent].append(child)
            in_degree[child] += 1
        
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            topsort.append(node)
            for adj in graph[node]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
        
        if len(topsort) == numCourses:
            return topsort
        else: return []