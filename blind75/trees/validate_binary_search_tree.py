# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def inorder(root, arr):
            if root:
                inorder(root.left, arr)
                arr.append(root.val)
                inorder(root.right, arr)
            return arr
        inorder_arr = inorder(root, arr)
        for i in range(0, len(inorder_arr)-1):
            if inorder_arr[i] >= inorder_arr[i+1]:
                return False
        else: return True
        