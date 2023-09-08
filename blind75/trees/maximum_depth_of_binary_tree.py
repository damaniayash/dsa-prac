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
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
'''
Base condition in when the traversal reaches leaf nodes we want to start a 0 hence retrun 0 in nit root condition.
Depth at each node is calculated as 1 + max(depth of left subtree, depth of right subtree)
Recursion is confusing for you, chart the recursion tree, it makes sense but you can't seem to write it on your own properly
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
