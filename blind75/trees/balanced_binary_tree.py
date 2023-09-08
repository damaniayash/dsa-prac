# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Revisit Max Depth first.
Main idea is to return a tuple(balanced, depth). Use bottom-up approach
Balanced -> check whether the tree is balanced up until that point. 
Check if the left and right subtrees are balanced and differnce in depth of the left and right subtrees <= 1.
Depth ->  also return 1 + max(depth of left subtree, depth of right subtree)
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return (True, 0)
            l_balanced, l_depth = traverse(node.left)
            r_balanced, r_depth = traverse(node.right)
            balanced = l_balanced and r_balanced and abs(l_depth - r_depth) <= 1
            return (balanced, 1 + max(l_depth, r_depth))
        return traverse(root)[0]