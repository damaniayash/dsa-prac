'''
BFS solution. same as number of island which a small change.
keep track of area of every island. This is done by counting the number of pops from the queue.
Compare the current island area with the max island area.
Reset current island area to 0 before the next bfs call..
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        queue = []
        island_area = 0

        def bfs(node):
            nonlocal island_area
            queue.append(node)
            while queue:
                X,Y = queue.pop(0)
                grid[X][Y] = 0
                island_area += 1
                for dx, dy in directions:
                    x = X + dx
                    y = Y + dy    
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        queue.append((x,y))
                        grid[x][y] = 0 
          
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_area = 0
                    bfs((r,c))
                    max_area = max(max_area, island_area)

        return max_area