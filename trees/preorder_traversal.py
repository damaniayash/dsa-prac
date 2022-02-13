# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Iterative
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return
        
        stack = deque()
        stack.append(root)
        
        ans = []
        
        while stack:
            
            node = stack.pop()
            ans.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left: 
                stack.append(node.left)
                
        return ans

    #Recursive
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        self.preOrder(root, li)
        return li
        
    def preOrder(self, root, li):
        if not root:
            return
        li.append(root.val)
        self.preOrder(root.left, li)
        self.preOrder(root.right, li)
        
    #def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:      
        # res = []
        # res1 = []
        # if root:
        #     res.append(root.val)
        #     res1 = res + self.preorderTraversal(root.left)
        #     res = res1 + self.preorderTraversal(root.right)
        # return res
        
        
        