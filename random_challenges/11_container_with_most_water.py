class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return area        
        
        
                