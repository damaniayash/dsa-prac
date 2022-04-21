class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        master = []
        for i in range(1,numRows+1):
            level = [0] * i
            level[0] = level[-1] = 1
            master.append(level)
        for i in range(0,len(master)):
            for j in range(0,len(master[i])):
                if master[i][j] == 0 and i > 1:
                    master[i][j] = master[i-1][j-1] + master[i-1][j]
        return master
                