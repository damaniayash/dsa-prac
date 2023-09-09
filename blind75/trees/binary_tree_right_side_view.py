# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = rights
from collections import deque
'''
Make sure you understand level-order traversal first.
This is basically level-order traversal but we only store the last element of the level (right-most node)s
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return None

        queue = deque([[root]])
        ans = [root.val]

        while queue:
            level = queue.popleft()
            next_level = []
            next_level_val = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                    next_level_val.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    next_level_val.append(node.right.val)
            if next_level:
                queue.append(next_level)
                ans.append(next_level_val[-1])

        return ans