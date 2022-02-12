# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import time
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        self.helper(root, postorder, inorder)
        return root
        
    def helper(self, node, postorder, inorder):
        if not postorder or not inorder:
            return
        
        node.val = postorder.pop()
        ind = inorder.index(node.val)
        # leftpost = []
        # for j,i in enumerate(postorder):
        #     if i in inorder[0:ind]:
        #         leftpost = leftpost + postorder[j : len(inorder[0:ind])]
        #         break
        # for i in postorder:
        #     if i in inorder[0:ind]:
        #         leftpost.append(i)
        # rightpost = []
        # for i in postorder:
        #     if i in inorder[ind+1:]:
        #         rightpost.append(i)
        # for j,i in enumerate(postorder):
        #     if i in inorder[ind+1:]:
        #         rightpost = rightpost + postorder[j : len(inorder[ind+1:])+1]
        #         break
        if len( inorder[ind+1:]) != 0:
            node.right = TreeNode()
            self.helper(node.right, postorder, inorder[ind+1:])
        if len(inorder[0:ind]) != 0:
            node.left = TreeNode() 
            self.helper(node.left, postorder, inorder[0:ind])
        
        
        