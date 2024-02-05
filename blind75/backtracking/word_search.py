'''
Run DFS for each letter on the board. We reset the visted set as empty set after each element.
We maintain a curr string and add the current element to it.
We also maintain a board_ptr which increases with every dfs call.
    This is used to check if the curr and word[: word_ptr] are the same.
    If they diverge we can simply return since that cannot be the solution.
If curr string and word are equal we have found the word and can store it.

Within the dfs call-
for every neighbour of the current node we check its boundary condition and make sure it is a new element.
we add the element to curr and visisted set.
Explore the current element 
After the dfs returns
we remove the last added element in curr and also remove it from the visited set.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        found = []
        visited = set()

        def dfs(node, word_ptr, curr, found):
            if curr != word[:word_ptr]:
                return
            if curr == word:
                print('Found', curr)
                found.append(True)
                return

            X, Y = node
            for dx, dy in directions:
                x, y = X + dx, Y + dy
                if 0 <= x < rows and 0 <= y < cols and (x,y) not in visited:
                    #print(curr, x,y, board[x][y], word_ptr, word[:word_ptr], visited)
                    curr += board[x][y]
                    visited.add(node)
                    dfs((x, y), word_ptr + 1, curr, found)
                    curr = curr[: -1]
                    visited.remove(node)

        for r in range(rows):
            for c in range(cols):
                dfs((r,c), 1, board[r][c], found)
                visited = set()

        if found == []:
            return False
        else:
            return True