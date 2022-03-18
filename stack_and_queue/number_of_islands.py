import numpy as np
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        grid_lx = np.matrix(grid).shape[0]
        #grid_lx = len(grid)
        grid_ly = np.matrix(grid).shape[1]
        #grid_ly = len(grid[0])
        for i in range(grid_lx):
            for j in range(grid_ly):
                grid[i][j] = int(grid[i][j])
                
        for i in range(grid_lx):
            for j in range(grid_ly):
                if grid[i][j] == 1:
                    self.bfs(grid,[i,j], grid_lx, grid_ly)
                    count+=1
        return count
    
    def bfs(self, grid, seed_index, grid_lx, grid_ly):  
        
        queue = []
        next_node_candidates = []
        queue.append(seed_index)
        
        while queue:
            
            curr_node = queue.pop(0)
            grid[curr_node[0]][curr_node[1]] = -1
            
            next_node_candidates.append([curr_node[0]+1, curr_node[1]])
            next_node_candidates.append([curr_node[0], curr_node[1]+1])
            next_node_candidates.append([curr_node[0]-1, curr_node[1]])
            next_node_candidates.append([curr_node[0], curr_node[1]-1])
            
            for next_node in next_node_candidates:
                
                if next_node[0] >= 0 and next_node[1] >= 0 and next_node[0] <= grid_lx-1 and next_node[1] <= grid_ly - 1 and grid[next_node[0]][next_node[1]] == 1:
                    
                    queue.append(next_node)
                    grid[next_node[0]][next_node[1]] = -1
                    
            next_node_candidates = []

        
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# import sys
# #np.set_printoptions(threshold=sys.maxsize)

# grid = [
#     ["1","1","1","1","0"],
#     ["1","1","1","1","1"],
#     ["1","1","1","1","0"],
#     ["1","1","1","1","1"]
# ]

# # grid = [
# #   ["1","1","0","0","0"],
# #   ["1","1","0","0","0"],
# #   ["0","0","1","0","0"],
# #   ["0","0","0","1","1"]
# # ]
# # grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
# #         ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
# #         ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
# #         ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
# #         ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
# #         ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
# #         ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
# #         ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
# #         ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
# #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
# #         ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
# #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
# #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
# #         ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
# #         ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
# #         ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
# #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
# #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
# #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
# #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]

# # for i in range(np.matrix(grid).shape[0]):
# #     for j in range(np.matrix(grid).shape[1]):
# #         grid[i][j] = int(grid[i][j])
# # print(np.matrix(grid))
# # cmapmine = ListedColormap(['b', 'r'], N=2)
# # fig, ax1 = plt.subplots(1, 1)
# # ax1.imshow(grid, cmap=cmapmine, vmin=0, vmax=1)
# # ax1.set_title('Land-Blue')
# # plt.show()


# #gridi = np.matrix(grid).shape[0]
# gridi = len(grid)
# #gridj = np.matrix(grid).shape[1]
# gridj = len(grid[0])
# for i in range(gridi):
#     for j in range(gridj):
#         grid[i][j] = int(grid[i][j])
# print(np.matrix(grid))
# count = 0
# def bfs(grid, seed_index):  
#     next_node_candidates = []
#     queue=[seed_index]
#     while queue:
#         curr_node = queue.pop(0)
#         grid[curr_node[0]][curr_node[1]] = -1
#         next_node_candidates.append([curr_node[0]+1, curr_node[1]])
#         next_node_candidates.append([curr_node[0], curr_node[1]+1])
#         next_node_candidates.append([curr_node[0]-1, curr_node[1]])
#         next_node_candidates.append([curr_node[0], curr_node[1]-1])
#         for next_node in next_node_candidates:
#             #print(next_node)
#             if next_node[0] >= 0 and next_node[1] >= 0 and next_node[0] <= gridi-1 and next_node[1] <= gridj-1 and grid[next_node[0]][next_node[1]] == 1:
#                 print(next_node)
#                 queue.append(next_node)
#                 grid[next_node[0]][next_node[1]] = -1
#         next_node_candidates = []
#         print('queue',np.matrix(queue))

# for i in range(gridi):
#     for j in range(gridj):
#         if grid[i][j] == 1:
#             bfs(grid,[i,j])
#             count+=1

# print(np.matrix(grid))
# print(count)



