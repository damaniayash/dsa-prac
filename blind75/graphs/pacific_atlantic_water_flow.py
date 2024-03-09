'''
Think inversely. Problem defines that water from how many cells can reach both pacific and atlantic ocean.
pacific ocen = top + left
atlantic ocean = bottom + right
Think that if there were a tsunami, how deep could the water reach inland. This is the same as water from middle flowing outwards.
Need to rever the condition for checking which cells are reachable.
Create two sets for each ocean and we have cells that get flooded with water from that ocen if there were a tsunami.
Then find the intersection of these two sets.
This gives us the cells with would get flooded by both pacific and atlantic ocean.
This intersection is also the set where if rain water falls, it will reach both the oceans.

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])

        top = [(0,i) for i in range(cols)]
        bottom = [(rows-1, i) for i in range(cols)]
        left = [(i,0) for i in range(rows)]
        right = [(i, cols-1) for i in range(rows)]

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        pacific_set = set()
        atlantic_set = set()

        def dfs(node, visited):

            if node in visited:
                return
            visited.add(node)
            
            X,Y = node
            for dx, dy in directions:
                x = dx + X
                y = dy + Y
                if 0 <= x < rows and 0 <= y < cols and heights[x][y] >= heights[X][Y]:
                    dfs((x,y), visited)
        
        pacific = top + left

        for node in pacific:
            dfs(node, pacific_set)

        atlantic = bottom + right

        for node in atlantic:
            dfs(node, atlantic_set)

        return list(atlantic_set.intersection(pacific_set))       



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



