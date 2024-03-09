class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        index = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(node):

            if node in visited:
                return 0
            if grid[node[0]][node[1]] == '0':
                return 0

            queue = [node]

            while queue:
                X,Y = queue.pop(0) 
                for dx, dy in index:
                    x = X + dx
                    y = Y + dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1' and (x,y) not in visited:
                        queue.append((x,y))
                        visited.add((x,y))
            return 1

        cnt = 0
        for i in range(rows):
            for j in range(cols):
                cnt += bfs((i,j))

        return cnt