class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(numbers)):
            if hashmap.get(target - numbers[i]) == None:
                hashmap[numbers[i]] = i 
            else:
                return [hashmap[target-numbers[i]]+1, i+1]