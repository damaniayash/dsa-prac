# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
We use a modified depth/height function for this. Bottom up approach.
The idea is to have the return value same as the max depth of subtree problem
But the calculate the depth of left subtree + depth of right subtree at every node.
Confusing problem, not an easy. read other materials as well for this problem
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(root):
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            nonlocal res
            res = max(res, l + r)
            print(root.val, res, l+r)
            return 1 + max(l,r)
        depth(root)
        return res
        