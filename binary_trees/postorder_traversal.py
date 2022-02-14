# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Iterative
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        stack = deque()
        stack.append(root)
        
        ans = []
        visited = []
        
        while stack:
            
            node = stack.pop()
            
            if node in visited:
                ans.append(node.val)
                
            elif not node.left and not node.right:
                ans.append(node.val)
                
            else:
                
                stack.append(node)
                    
                if node.right:
                    stack.append(node.right)
                
                if node.left: 
                    stack.append(node.left)
                    
                visited.append(node)
                
        return ans
    #Recursive
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     li = []
    #     self.preorder(root, li)
    #     return li
    
    # def preorder(self, root, li):
    #     if root == None:
    #         return
    #     self.preorder(root.left, li)
    #     self.preorder(root.right, li)
    #     li.append(root.val)
        