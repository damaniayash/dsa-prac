class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(0,len(nums)):
            if nums[i] == val:
                count += 1
        for _ in range(0, count):
            nums.remove(val)
        return len(nums)