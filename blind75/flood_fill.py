class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # store the original color before dfs
        og_color = image[sr][sc]

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            X,Y = node
            # replace the color of the cell
            image[X][Y] = color
            for dx, dy in directions:
                x,y = X + dx, Y + dy
                if 0 <= x < rows and 0 <= y < cols: # check for bounds
                    # Making saure to select only those neighbors that are of the same color as the 
                    # original cell where floodfill started
                    if image[x][y] == og_color: 
                        dfs((x,y))
        
        dfs((sr,sc))
        #print(image)
        return image

