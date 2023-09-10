# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Inorder traversal for BST is always sorted.
So kth smallest element is (k-1)th element in inorder list.
k-1 beacuse list is 0 indexed whereas question assumes k is 1 indexed.
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inorder(root, arr):
            if root:
                inorder(root.left, arr)
                arr.append(root.val)
                inorder(root.right, arr)
            return arr

        return inorder(root, arr)[k-1]