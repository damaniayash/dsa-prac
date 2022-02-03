# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
        