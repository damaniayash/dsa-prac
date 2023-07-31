'''
L --- M --- H
if L < M   --> left partition is sorted. Now check if the target is within this sorted left partiton.
   if yes just move high = mid - 1 because we know that the target is to the left of mid.
   else the target is to the right side of mid so low = mid + 1
if M < H   --> right partiton is sorted. Check if the target within this sorted right partition
   if yes move low = mid - 1 because we know that the target is the right side of mid.
   else the target is to the left side of mid so high = mid - 1.
 Note: The <= / >= in the elfi statememts ensure that the code works when low/mid or mid/high are the same index.   
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
