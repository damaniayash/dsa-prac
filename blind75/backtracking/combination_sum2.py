
'''
For loop solution
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, curr):

            if sum(curr) > target:
                return
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            for x in range(i, len(candidates)):
                if x > i and candidates[x] == candidates[x - 1]:
                    continue
                curr.append(candidates[x])
                dfs(x + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return res

            