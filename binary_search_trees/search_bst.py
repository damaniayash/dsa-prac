# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #Iterative
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        while root:
            
            if val == root.val:
                return root
                
            elif val > root.val:
                root = root.right
                
            else:
                root = root.left
                
                
#     #Recursive
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
#         ans = []
#         self.helper(root, val, ans)
#         if ans:
#             return ans[0]
#         return None
        
#     def helper(self, node, val, ans):
        
#         if not node:
#             return
        
#         elif val == node.val:
#             ans.append(node)
#             return
        
#         elif val > node.val:
#             self.helper(node.right, val, ans)
            
#         else:
#             self.helper(node.left, val, ans)
            
    
    
        
    
                

            