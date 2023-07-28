'''
Use binary search twice. First search is to find the row containing target.
Then perform a binary search on the row 
'''
class Solution:
    def binary_search_row(self, matrix, target):
            low, high = 0, len(matrix) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif target > matrix[mid][-1]:
                    low = mid + 1
                elif target < matrix[mid][0]:
                    high = mid - 1
            return -1
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = self.binary_search_row(matrix, target)
        if target_row == -1: 
            return False
        else:
            nums = matrix[target_row]
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if target == nums[mid]:
                    return True
                elif target > nums[mid]:
                    low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
            return False
