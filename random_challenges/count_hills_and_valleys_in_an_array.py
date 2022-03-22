from collections import deque
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        #nums = list(dict.fromkeys(nums))
        nums.append(0)
        nums_new = deque([])
        for i in range(0,len(nums)-1):
            if nums[i] != nums[i+1]:
                nums_new.append(nums[i])

        count = 0
        for i in range(1, len(nums_new) - 1):
            if nums_new[i] > nums_new[i+1] and nums_new[i] > nums_new[i-1]:
                count += 1
                #print('hill')
            elif nums_new[i] < nums_new[i+1] and nums_new[i] < nums_new[i-1]:
                count += 1
                #print('valley')
        return count