'''
Create a recursive tree by either selecting or not selecting an element and make the recursive call
return the calls when current index exceeds the len of nums.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # selecting the number and exploring the tree
            subset.append(nums[i])
            dfs(i + 1)
            
            # NOT selecting the number and exploring the tree.
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        