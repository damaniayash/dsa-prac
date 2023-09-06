# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Use Preorder traversal. For each node swap its left and right children.
It is this simple, draw out/ follow the recursion for better understanding
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def preorder(root):
            if root:
                root.right, root.left = root.left, root.right
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return root