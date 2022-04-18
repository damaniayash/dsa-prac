class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_value = max(nums)
        max_index = nums.index(max_value)
        nums.remove(max_value)
        for i in nums:
            if i > max_value//2:
                return -1
        return max_index