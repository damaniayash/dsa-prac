# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    
    def sumpath(self,root,currsum,targetSum,answer):
        if root == None:
            return
        if root.left == None and root.right == None:
            #print(root.val + currsum)
            if root.val + currsum == targetSum:
                answer.append(root.val + currsum)
        self.sumpath(root.left, currsum+root.val, targetSum,answer)
        self.sumpath(root.right, currsum+root.val, targetSum,answer)
            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        currsum = 0
        answer = []
        self.sumpath(root, currsum , targetSum, answer)
        #print(answer)
        if targetSum in answer:
            return True
        else:
            return False
        
        
        