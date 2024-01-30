'''
Neetcode solution
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def dfs(i, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return 
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return ans
    
'''
Bounding condition - 
1. If the sum of the subset exceeds the target return 
2. If we find the sum of subset == target return

eg. [1,2,3,4]

dfs calls - 
[consider 1,2,3,4]  [consider 2,3,4] [consider 3,4] [consider 4]
The for loop's starting i decreases for every nex branch.
We need to pop after the dfs call to clear the last element for the next call.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def dfs(i, subset):
            if sum(subset) > target:
                return
            elif sum(subset) == target:
                ans.append(subset.copy())
                return 

            for x in range(i, len(candidates)):
                subset.append(candidates[x])
                dfs(x, subset)
                subset.pop()
            
        dfs(0, [])
        return ans
        