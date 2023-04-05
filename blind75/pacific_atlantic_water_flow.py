class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # print(rows, cols)
        pac, atl  = [], []

        # ADD TOP ROW
        for i in range(cols): pac.append((0,i))
        # ADD LEFTMOST COLUMN
        for i in range(rows): pac.append((i,0))
        # ADD BOTTOM ROW
        for i in range(cols): atl.append((rows - 1, i))
        # ADD RIGHTMOST COLUMN
        for i in range(rows): atl.append((i, cols - 1))

        # print(pac)
        # print(atl)

        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        visited_pac = set()
        visited_atl = set()
        
        # def dfs(node, v):
        #     v.add(node)
        #     X,Y = node
        #     for dx,dy in neighbors:
        #         x, y = X + dx, Y + dy
        #         if 0 <= x < rows and 0 <= y < cols and heights[x][y] >= heights[X][Y]:
        #             if (x,y) not in v:
        #                 v.add((x,y))
        #                 dfs((x,y),v)

        def dfs(node, v):
            if node in v:
                return 
            v.add(node)
            X,Y = node
            for dx,dy in neighbors:
                x, y = X + dx, Y + dy
                if 0 <= x < rows and 0 <= y < cols and heights[x][y] >= heights[X][Y] and (x,y) not in v:
                    dfs((x,y),v)
        
        for i in pac:
            dfs(i, visited_pac)
            
        for i in atl:
            dfs(i, visited_atl)

        # print(visited_pac)
        # print(visited_atl)

        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in visited_pac and (i,j) in visited_atl:
                    res.append([i,j])
        return res



