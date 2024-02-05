'''
Neetcode Solution - sort the list and increment the pointer when the enxt element is the same.
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        curr = []

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return curr

            # Selecting the value 
            curr.append(nums[i])
            dfs(i + 1, curr)

            # NOT selecting the value
            curr.pop()
            # traverse to ignore duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i + 1, curr)

        dfs(0, [])
        return res
            
'''

'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []

        def dfs(i, curr):
            ans.append(curr.copy())
        
            for x in range(i, len(nums)):
                if x > i and nums[x] == nums[x - 1]:
                    continue
                curr.append(nums[x])
                dfs(x + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return ans