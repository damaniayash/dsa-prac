from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):

        rows, cols = len(rooms), len(rooms[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        queue = deque()
        num_gates = 0

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    num_gates += 1
                    queue.append((r,c))
        
        if num_gates == 0:
            return
         
        time = 0
        nodes = []
        while queue:
            print(queue)
            time += 1
            while queue:
                popped = queue.popleft()
                nodes.append(popped)
        
            print('after popping', queue)
            for node in nodes:
                X, Y = node
                for dx, dy in directions:
                    x = X + dx
                    y = Y + dy
                    if 0 <= x < rows and 0 <= y < cols and rooms[x][y] == 2147483647:
                        rooms[x][y] = time
                        queue.append((x,y))
            
            
        
        print(rooms)


            
