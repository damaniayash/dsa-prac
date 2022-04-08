from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        lenx, leny = len(mat), len(mat[0])
        for i in range(0,lenx):
            for j in range(0,leny):
                if mat[i][j] != 0:
                    self.helper([i,j], mat, lenx, leny)
        return mat
    
    def helper(self, seed, mat, lenx, leny):
        queue = deque()
        count = 0
        queue.append(seed)
        while queue:
            pop = queue.popleft()
            c_list = []
            c_list.append([ pop[0]+1, pop[1] ])
            c_list.append([ pop[0]-1, pop[1] ])
            c_list.append([ pop[0], pop[1]+1 ])
            c_list.append([ pop[0], pop[1]-1 ])
            for c in c_list:
                if c[0] >= 0 and c[0] < lenx and c[1] >= 0 and c[1] < leny:
                    if mat[c[0]][c[1]] == 0:
                        mat[seed[0]][seed[1]] = abs(c[0] - seed[0]) + abs(c[1] - seed[1])
                        return
                    queue.append([c[0],c[1]])  