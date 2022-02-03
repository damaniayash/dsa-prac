# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
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
        
        
        