#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
'''
This is BFS for trees.
Initialize queue with root node.
Inside while loop
pop item from queue, add left and right node to a list called next_level if they are not None.
Append this next_level list to the queue.
We want val as the answer so store the values in a seperate list called next_level_list
return ans
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return None

        queue = deque([[root]])
        ans = [[root.val]]

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
                ans.append(next_level_val)

        return ans