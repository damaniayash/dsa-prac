class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]

        num_rotten, num_fresh = 0, 0
        queue = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    num_rotten += 1
                    queue.append((r,c))
                if grid[r][c] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        if num_rotten == 0:
            return -1

        time = 0
        while True:
            
            nodes = []
            while queue:
                popped = queue.pop(0)
                nodes.append(popped)
            #print('popped', nodes)
            #print(time, queue)
            
            for node in nodes:
                #print('node:', node)
                X,Y = node
                for dx, dy in directions:
                    x, y = X+dx, Y+dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        queue.append((x,y))
                        grid[x][y] = 2
                        
            nodes = []
            #print('added child', queue)
            if len(queue) == 0:
                break

            time += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    #print('found fresh')
                    return -1
        
        #print('time', time)
        return time
        



