# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inorderlist = []
        
        self.inorder(root, inorderlist)
        
        for i in range(0, len(inorderlist)-1):
            
            if inorderlist[i] >= inorderlist[i+1]: return False
            
        return True
            
    def inorder(self, node, inorderlist):
        
        if not node:
            return
        
        self.inorder(node.left, inorderlist)
        
        inorderlist.append(node.val)
        
        self.inorder(node.right, inorderlist)
        