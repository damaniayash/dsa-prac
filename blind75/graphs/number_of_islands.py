from collections import deque
class Solution:

    # DFS APPROACH
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        rows, cols = len(grid), len(grid[0])

        def dfs(node):
            X,Y = node
            for dx,dy in neighbours:
                x = X + dx
                y = Y + dy
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                    grid[x][y] = '0'
                    dfs((x,y))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    dfs((i,j))
                    cnt += 1
        return cnt


    # BFS APPROACH
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        q = deque()
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        rows, cols = len(grid), len(grid[0])

        def bfs(node):
            q.append(node)
            while q:
                X,Y = q.popleft()
                for dx,dy in neighbours:
                    x = X + dx
                    y = Y + dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                        grid[x][y] = '-1'
                        q.append((x,y))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    bfs((i,j))
                    cnt += 1
        return cnt


    # ITERATICE DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        stack = deque()
        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        cnt = 0

        def dfs(node):
            stack.append(node)
            visited.add(node)
            while stack:
                X,Y = stack.pop()
                #print(X,Y)
                for dx,dy in neighbors:
                    x = X + dx
                    y = Y + dy
                    if 0 <= x < rows and 0 <= y < cols and (x,y) not in visited and grid[x][y] == '1':
                        grid[x][y] = '0'
                        stack.append((x,y))
                        visited.add((x,y))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    dfs((i,j))
                    cnt += 1
        
        return cnt