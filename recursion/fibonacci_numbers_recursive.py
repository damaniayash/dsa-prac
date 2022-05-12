class Solution:
    # def fib(self, n: int) -> int:
    #     if n == 0: return 0
    #     elif n == 1: return 1
    #     else: return self.fib(n-1) + self.fib(n-2)
            
    def fib(self, n: int) -> int:
        hashmap = {}
        result = self.helper(n, hashmap)
        return result
        
    def helper(self, n, hashmap):
        if n in hashmap:
            return hashmap[n]
        if n == 0:
            hashmap[0] = 0
            return 0
            
        elif n == 1:
            hashmap[1] = 1
            return 1
        else:
            result = self.helper(n-1, hashmap) + self.helper(n-2, hashmap)
        
        hashmap[n] = result
        return result