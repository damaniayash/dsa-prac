'''
The problem statement is a little vague.
Basically we need to make all 'O' that are completely surronded by 'X' to 'X' as well.
The 'O' on the top, bottom, left, right are open from atleast one side thus they can never be completely surronded by 'X'.
Using this idea if we apply DFS/ BFS to the 'O' that are in the top, bottom, left, right. These 'O' can also not be converted to 'X's.
So first we mark all the 'O' in the top left right bottom as 'P'.
This way we can perform DFS/BFS on all the 'P'. All the 'P's after DFS/BFS are the ones that can never be completely surronded by 'X'.
Then convert all the 'O' to 'X'. All the remaining 'O' are surrounded by 'X'.
Finally convert all the 'P' back to 'O'.
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        top = [(0, i) for i in range(0, cols)]
        bottom = [(rows-1, i) for i in range(0, cols)]
        left = [(i, 0) for i in range(0, rows)]
        right = [(i, cols-1) for i in range(0, rows)]
        index = [(0,1), (0,-1), (1,0), (-1,0)]


        def dfs(node):
            queue = [node]
            board[node[0]][node[1]] = 'P'
            while queue:
                X,Y = queue.pop(0)
                for dx, dy in index:
                    x = X + dx
                    y = Y + dy
                    if 0 <= x < rows and 0 <= y < cols and board[x][y] and board[x][y] == 'O':
                        queue.append((x,y))
                        board[x][y] = 'P'

        border = [top, bottom, left, right]
        for j in border:
            for i in j:
                x,y = i
                if board[x][y] == 'O':
                    dfs((x, y))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'P':
                    board[r][c] = 'O'
        
        """
        Do not return anything, modify board in-place instead.
        """
        