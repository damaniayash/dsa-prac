# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder_list = []
        self.inorder(root, inorder_list)
        root = inorder_list[0]
        for i in range(0, len(inorder_list)-1):
            inorder_list[i].right =  inorder_list[i+1]
            inorder_list[i].left = None
        inorder_list[-1].right = None
        inorder_list[-1].left = None
        return root
            
        
    def inorder(self, root, inorder_list):
        if root:
            self.inorder(root.left, inorder_list)
            inorder_list.append(root)
            self.inorder(root.right, inorder_list)