class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            if hashmap.get(target - nums[i]) != None:
                return [i,hashmap.get(target - nums[i])]
            hashmap[nums[i]] = i