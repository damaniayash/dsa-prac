class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = {}
        return self.helper(n, hashmap)
        
    def helper(self, n, hashmap):
        if n in hashmap:
            return hashmap[n]
        elif n in [1,2]:
            return n
        else:
            result = self.helper(n-1, hashmap) + self.helper(n-2, hashmap)
        hashmap[n] = result
        return result
        