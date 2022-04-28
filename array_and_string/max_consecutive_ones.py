class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        if 1 not in nums:
            return 0
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] == 1:
                current_count += 1
                max_count = max(max_count,current_count)
            else:
                current_count = 0
            #print(max_count, current_count)
        return max_count + 1