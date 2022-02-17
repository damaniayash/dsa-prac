# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        node = root
        
        while True:
            
            if node.val > val:
                
                if node.left:
                    node = node.left
                    
                else:
                    node.left = TreeNode(val)
                    break
                    
            else:
                
                if node.right:
                    node = node.right
                    
                else:
                    node.right = TreeNode(val)
                    break
                    
        return root
                
        
        
        
        
                    
            
        
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
#         if not root:
#             root = TreeNode()
#             root.val = val
#             return root
        
#         elif not root.left and root.val > val:
#             root.left = TreeNode()
#             root.left.val = val
#             return root
        
#         elif not root.right and root.val < val:
#             root.right = TreeNode()
#             root.right.val = val
#             return root
        
#         node = root
        
#         while True:
            
#             if not node.left and not node.right:
#                 break
            
#             elif not node:
#                 return 
                        
#             elif node.val < val and node.right:
#                 node = node.right
                
#             elif node.val > val and node.left:
#                 node = node.left
        
#         if node.val < val:
#             node.right = TreeNode()
#             node.right.val = val
            
#         else:
#             node.left = TreeNode()
#             node.left.val = val
            
#         return root