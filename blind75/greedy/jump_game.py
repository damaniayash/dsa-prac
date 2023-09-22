'''
The idea is to traverse backwards from the end of the array.
At each step we check whether the whether we can reach the target from the current element.
If we can reach the target, the current element beacomes out new target.
nums[i] > target - i -> This checks whether current element has enough jumps to reach the target.
If it does this becomes our new target.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= target - i:
                target = i

        if target == 0: return True
        else: return False