from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = deque()
        lenx, leny = len(image), len(image[0])
        i = self.helper(image, sr, sc, lenx, leny, newColor, queue)
        if i:
            return i
        return image
        
    def helper(self, image, i, j, lenx, leny, newColor, queue):
        c_list = []
        oldColor = image[i][j]
        image[i][j] = newColor
        if oldColor == newColor:
            return image
        queue.append([i,j])
        while queue:
            temp = queue.popleft()
            image[temp[0]][temp[1]] = newColor
            c_list.append([temp[0]-1,temp[1]])
            c_list.append([temp[0]+1,temp[1]])
            c_list.append([temp[0],temp[1]+1])
            c_list.append([temp[0],temp[1]-1])
            for c in c_list:
                if c[0] >= 0 and c[0] < lenx and c[1] >= 0 and c[1] < leny:
                    if image[c[0]][c[1]] == oldColor:
                            image[c[0]][c[1]] = newColor
                            queue.append([c[0],c[1]])
            c_list = []
    
            