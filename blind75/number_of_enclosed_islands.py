class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        # Approach
        # Do FLOODFILL from the borders where grid is 0 (border island) and make them 1.
        # This is beacuse the border island will never be fully enclosed by water so treat them as water.
        # Now this become the number of islands question.
        # Apply DFS on all islands and increment counter.

        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()

        def flood_fill(node):
            if node in visited:
                return
            visited.add(node)
            X,Y = node
            grid[X][Y] = 1
            for dx, dy in directions:
                x,y = X + dx, Y + dy
                if 0 <= x < rows and 0 <= y < cols:
                    if grid[x][y] == 0:
                        flood_fill((x,y))
        def dfs(node):
            X,Y = node
            grid[X][Y] = 1
            for dx, dy in directions:
                x,y = X + dx, Y + dy
                if 0 <= x < rows and 0 <= y < cols:
                    if grid[x][y] == 0:
                        dfs((x,y))


        border_nodes = []
        for i in range(cols): border_nodes.append((0, i))
        for i in range(cols): border_nodes.append((rows - 1 , i))    
        for i in range(rows): border_nodes.append((i, 0))
        for i in range(rows): border_nodes.append((i, cols - 1))

        for x,y in border_nodes:
            if grid[x][y] == 0:
                flood_fill((x,y))

        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dfs((i,j))
                    cnt += 1
        return cnt

        
        
        
    
