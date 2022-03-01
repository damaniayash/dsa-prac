# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        node_p, node_q = root, root
        
        while node_p.val == node_q.val:
            
            ans = node_p
            
            if node_p.left and node_p.val > p.val:
                node_p = node_p.left
            elif node_p.right and node_p.val < p.val:
                node_p = node_p.right
            
            if node_q.left and node_q.val > q.val:
                node_q = node_q.left
            elif node_q.right and node_q.val < q.val:
                node_q = node_q.right
                
        return ans
            
                
                