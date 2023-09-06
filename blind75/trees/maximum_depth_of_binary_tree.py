# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Intialize depth as 1. Keep adding 1 to depth until we encounter leaf node.
Compare the accumulated depth with maxdepth and select the higest.
For empty trees, since the root is null, it will skip preorder function and return 0 (default maxdepth value)
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth, depth = 0, 1
        def preorder(root, depth):
            if root:
                nonlocal maxdepth
                if not root.left and not root.right:
                    maxdepth = max(depth, maxdepth)
                preorder(root.left, depth + 1)
                preorder(root.right, depth + 1)
        preorder(root, depth)
        return maxdepth