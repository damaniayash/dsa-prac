class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums = str(num)
        print(len(nums))
        cnt = 0
        for i in range(0, len(nums)-(k-1)):
            #print(x)
            temp = '0'*k
            if nums[i:i+k] == temp:
                continue
            x = int(nums[i:i+k].lstrip('0'))
            #print(x)
            if num % x == 0:
                cnt += 1
        return cnt
            
            