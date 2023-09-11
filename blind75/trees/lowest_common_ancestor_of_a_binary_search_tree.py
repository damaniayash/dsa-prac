# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
The idea is to find a node where the divergence began.
So while p.val == q.val, we do regular BST search for both p and q simultaneously.
This loop will stop at the stage where p and q search traversal diverge.
By definition this is the lca of the BST.
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        root_p, root_q = root, root
        res = root

        while root_p.val == root_q.val:

            res = root_p

            if root_p.left and root_p.val > p.val:
                root_p = root_p.left
            elif root_p.right and root_p.val < p.val:
                root_p = root_p.right

            if root_q.left and root_q.val > q.val:
                root_q = root_q.left
            elif root_q.right and root_q.val < q.val:
                root_q = root_q.right
                
        return res