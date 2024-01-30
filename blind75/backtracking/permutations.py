'''
            []
    [1]      [2]       [3]
  [2] [3]  [1] [3]   [1] [2]
  [3] [2]  [3] [1]   [2] [1]

bounding function -  return when len of curr == len of nums.
Maintain a set of the elements added to curr so that we do not repeat element.
Iterate [0, len(nums)]
    check if the element in present in curr. We want new elements.
    add to used and curr
    call dfs
    remove from used and curr.

the for loop in dfs makes sure that we takes all the elements one by one and the if check condition
will prevent us from considering same element twice.
we remove the element from curr because that part of the tree is already explored and
we want to reset it back to previous state.
Neetcode solution for this promlem is a bit confusing. use this instead. - 
https://leetcode.com/discuss/study-guide/1405817/backtracking-algorithm-problems-to-practice    
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def dfs(i, curr, used):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return 
            
            for i in range(0, len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    curr.append(nums[i])
                    dfs(i, curr, used)
                    used.remove(nums[i])
                    curr.pop()

        dfs(0, [], set())
        return ans