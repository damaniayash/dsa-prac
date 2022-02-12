# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        self.helper(root, preorder, inorder)
        return root
        
    def helper(self, node, preorder, inorder):
        if not preorder or not inorder:
            return 
        node.val = preorder.pop(0)
        ind = inorder.index(node.val)
        if len(inorder[0:ind]) != 0:
            node.left = TreeNode()
            self.helper(node.left, preorder, inorder[0:ind])
        if len(inorder[ind+1:]) != 0:
            node.right = TreeNode()
            self.helper(node.right, preorder, inorder[ind+1:])