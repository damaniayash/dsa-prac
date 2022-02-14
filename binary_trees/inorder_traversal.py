# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
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
                # RIGHT -> DATA -> LEFT
                if node.right:
                    stack.append(node.right)
                    
                stack.append(node)
                
                if node.left: 
                    stack.append(node.left)
                    
                visited.append(node)
                
        return ans
        
    #Recursive
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        self.inorder(root, li)
        return li
        
    def inorder(self, root, li):
        if root == None:
            return
        self.inorder(root.left, li)
        li.append(root.val)
        self.inorder(root.right, li)
        