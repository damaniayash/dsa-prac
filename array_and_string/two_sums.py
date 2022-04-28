class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0, len(numbers)):
            no2 = target - numbers[i]
            if self.binary_search(numbers, no2)[0]:
                ans.append(i+1)
                ans.append(self.binary_search(numbers, no2)[1] + 1)
                break
            count = 1
        if ans[0] == ans[1]:
            ans[1] = ans[1] + 1
        return ans
            
        
    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high:
            mid = (low + high) // 2 
            if target == nums[mid]:
                return True, mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
        else:
            return False, mid
            