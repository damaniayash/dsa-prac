# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(p, q):
            if p == q == None:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return sametree(p.left, q.left) and sametree(p.right, q.right)
            
        if not root:
            return False
        if sametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        same, arr = False, []
        def traverse(root, subRoot):
            nonlocal same, arr
            if root:
                if root.val == subRoot.val:
                    same = sametree(root, subRoot)
                    arr.append(same)
                traverse(root.left, subRoot)
                traverse(root.right, subRoot)
            return same, arr

        def sametree(p, q):
            if p == q == None:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return sametree(p.left, q.left) and sametree(p.right, q.right)
        _, arr = traverse(root, subRoot)
        if True in arr:
            return True
        else:
            return False
        