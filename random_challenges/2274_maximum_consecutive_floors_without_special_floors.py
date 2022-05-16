class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:

        special = sorted(special)

        max_con = 0
        max_con = max(max_con, special[0] - bottom)

        for i in range(0, len(special)-1):
            max_con = max(max_con, special[i+1] - special[i]-1)

        max_con = max(max_con, top-special[-1])
        
        return max_con
            