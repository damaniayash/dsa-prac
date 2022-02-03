# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        self.preorder(root, li)
        return li
    
    def preorder(self, root, li):
        if root == None:
            return
        self.preorder(root.left, li)
        self.preorder(root.right, li)
        li.append(root.val)
        