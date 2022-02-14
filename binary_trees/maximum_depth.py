# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
answer = 0
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #       Iterative
        
        if root == None:
            return 0
        level = []
        level.append(root)
        cnt = 0
        while level:
            cnt+=1
            nextlevel = []
            for i in level:
                if i.left != None:
                    nextlevel.append(i.left)
                if i.right != None:
                    nextlevel.append(i.right)
            level = nextlevel
        return cnt
    
        #       Recursive
        
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
                
            
            
        