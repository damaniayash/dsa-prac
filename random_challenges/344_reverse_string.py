class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low, high = 0, len(s)-1
        while high > low:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        
        