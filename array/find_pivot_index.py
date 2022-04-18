class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_list = [0] * len(nums)
        r_list = [0] * len(nums)
        sum = 0
        
        # Create l_list -> Array of increasing sums from left to right
        # Create r_list -> Array of increasing sums from right to left
        
        for i in range(0,len(nums)):
            sum += nums[i]
            l_list[i] = sum
        sum = 0
        for i, e in reversed(list(enumerate(nums))):
            sum += nums[i]
            r_list[i] = sum
        
        # If only 1 element, return the element 
        if len(nums) == 1:
            return nums[0]
        
        # Left Edge case
        elif r_list[1] == 0:
            return 0
        
        # Check for every index if l_list[i-1] and r_list[1+1], if equal then return i 
        for i in range(1, len(nums) - 1):
            if l_list[i-1] == r_list[i+1]:
                return i
            
        # Right Edge case
        if l_list[-2] == 0:
            return len(nums) - 1
        
        # No target found, return -1
        else:
            return -1     