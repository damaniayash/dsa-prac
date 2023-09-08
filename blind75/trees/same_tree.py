# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
If both p and q are None -> return True since technically they are the same
If either p or q is None -> return False. Only one of the node is None, tree cannot be equal.
At this stage p and q are gaurantted to not be None. Only way they could differ is if thier values were not equal
So we check if the value are the same, if not return False.
traverse(p.left, q.left) and traverse(p.right, q.right) -> we want both the left and the right subtrees to be same. 
Better watch neetcode if you do not understand this comment.
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(p, q):
            if p == q == None:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return traverse(p.left, q.left) and traverse(p.right, q.right)
        return traverse(p, q)