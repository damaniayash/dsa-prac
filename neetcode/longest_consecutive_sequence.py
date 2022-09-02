class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        longest = 0
        
        for i in nums:
            if (i-1) not in numset:
                length = 0
                while (i + length) in numset:
                    length += 1
                longest = max(longest, length)
        return longest
        
        
        # # Sort and check consecutive elements (n log n)
        # if not nums:
        #     return 0
        # nums =  sorted(list(set(nums)))
        # print(nums)
        # maxcnt = 0
        # cnt = 0
        # for i in range(0,len(nums)-1):
        #     if nums[i+1] - nums[i] == 1:
        #         cnt += 1
        #     else:
        #         cnt = 0
        #     maxcnt = max(cnt, maxcnt)
        # return maxcnt+1
        
        