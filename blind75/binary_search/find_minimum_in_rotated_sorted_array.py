'''
Look for partiton containing the pivot point.
if low > mid -> the left side partiton has pivot point so move high = mid
if mid > high -> the right side partiton has the pivot point so move low = mid
when low - high == 1 means that we have reached the pivot point. So return the min(nums[low], nums[high)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums) - 1
        while low - high <= 1:
            mid = (low + high) // 2
            if high - low == 1:
                return min(nums[low], nums[high])
            elif nums[low] < nums[mid] < nums[high]:
                return nums[0]
            elif nums[mid] < nums[low]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid
