# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Watch neetcode.
Idea is that calc of max path sum is diff and the return value is diff.
We return the root.val + max from left subtree OR max from right subtree.
    We only consider one of the sides since we cannot split the while traversing.
the ans is max(ans, root + max from left + max from right).
We calculate the sum of root + left + right for ans and return root + max(left,right)
    Since we can other have either left OR right for return value since we want to maintain a linear
    path so we cannot split i.e have both left and right in the return value but
    calculate them for max path sum
'''
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -math.inf
        def traverse(root):
            nonlocal ans
            if not root:
                return 0
            l = traverse(root.left)
            r = traverse(root.right)
            lmax, rmax = max(l,0), max(r,0)
            curr_sum = root.val + max(lmax, rmax)
            ans = max(ans, root.val + lmax + rmax)
            return curr_sum
        traverse(root)
        return ans
                           
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -math.inf
        def traverse(root):
            nonlocal max_path_sum
            if not root:
                return 0
            l = traverse(root.left)
            r = traverse(root.right)
            curr_sum = max(root.val+l, root.val+r, root.val)
            max_path_sum = max(curr_sum, max_path_sum, root.val + l + r)
            return curr_sum
        traverse(root)
        return max_path_sum