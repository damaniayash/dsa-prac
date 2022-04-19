# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_list = []
        self.inorder(root, inorder_list)
        return inorder_list[k-1]
        
    def inorder(self, node, inorder_list):
        if node:
            self.inorder(node.left, inorder_list)
            inorder_list.append(node.val)
            self.inorder(node.right, inorder_list)
        