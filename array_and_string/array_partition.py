class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum(nums[0::2])
        # sum = 0
        # for i in range(0,len(nums),2):
        #     sum += min(nums[i],nums[i+1])
        # #print(nums[0::2])
        # return sum
            