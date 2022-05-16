class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        divider, cnt = 0, 0
        s1, s2 = 0, sum(nums)
        for i in range(0, len(nums)-1):
            s1 += nums[divider]
            s2 -= nums[divider]
            divider += 1
            if s1 >= s2:
                cnt += 1
        return cnt
            
        # divider, cnt = 1,0
        # for i in range(0, len(nums)-1):
        #     s1 = nums[0:divider]
        #     s2 = nums[divider:]
        #     divider += 1
        #     if sum(s1) >= sum(s2):
        #         cnt += 1
        #     print(s1,s2)
        # return cnt