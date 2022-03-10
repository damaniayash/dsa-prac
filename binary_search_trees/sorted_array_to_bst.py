# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: 
        
        b_root = self.build_tree(None, nums)
        return b_root
        
    def build_tree(self, root, nums):
        
        if len(nums) == 0:
            return
        
        m_ind = len(nums)//2
        
        if root == None: root = TreeNode(nums[m_ind])
            
        else: self.insert(root, nums[m_ind])
            
        self.build_tree(root, nums[0:m_ind])
        self.build_tree(root, nums[m_ind+1:])
        
        return root
    
    def insert(self, root, target):
        
        node = root
        
        while True:
            
            if target < node.val:
                
                if node.left:
                    node = node.left
                    
                else:
                    node.left = TreeNode(target)
                    break
                    
            else:
                
                if node.right:
                    node = node.right
                    
                else:
                    node.right = TreeNode(target)
                    break
        
