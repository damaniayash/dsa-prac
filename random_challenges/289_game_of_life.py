class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        count_arr = []
        lenx = len(board)
        leny = len(board[0])

        for i in range(0, lenx):
            for j in range(0, leny):
                n_list = []
                n_list.append([i, j+1])
                n_list.append([i, j-1])
                n_list.append([i+1, j])
                n_list.append([i-1, j])
                n_list.append([i+1, j+1])
                n_list.append([i+1, j-1])
                n_list.append([i-1, j+1])
                n_list.append([i-1, j-1])
                count_1 = 0
                for n in n_list:
                    if n[0] >= 0 and n[0] < lenx and n[1] >= 0 and n[1] < leny:
                        if board[n[0]][n[1]] == 1:
                            count_1 += 1
                count_arr.append(count_1)
        ind = 0
        for i in range(0, lenx):
            for j in range(0, leny):
                if board[i][j] == 1:
                    if count_arr[ind] < 2:
                        board[i][j] = 0
                    elif count_arr[ind] > 3:
                        board[i][j] = 0
                else:
                    if count_arr[ind] == 3:
                        board[i][j] = 1
                ind += 1

        