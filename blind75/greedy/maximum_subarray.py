'''
Use Kadana's algorith to solve this.
At each time step the curr_sum of the subarray sum is
curr_sum = max(A[i], A[i] + curr_sum)
It is not as intuitive but it works. 
Draw out few iteraitons for better understanding.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = max(num, num + curr_sum)
            max_global = max(curr_sum, max_global)
        return max_global