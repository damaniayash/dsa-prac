# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, prev_max):
            if not node:
                return 0
            # add is set to one if good node is detected and prev_max is updated
            if node.val >= prev_max:
                add = 1
                prev_max = max(prev_max, node.val)
            else:
                add = 0
            l = traverse(node.left, prev_max)
            r = traverse(node.right, prev_max)
            return add + l + r

        return traverse(root, root.val)