# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Make sure you understand same tree problem first.
if subRoot is empty -> It can still be considered as subtree of root (leaf nodes)
if root is empty and subRoot is not -> root cannot contain subroot in this case so return False
if the root.val and subRoot.val are equal we can call the sametree function
    if that function return true that means the subtrees are identical

we want to traverse the entire root tree and see whether any subroot tree nodes are equal to the current node
then call same tree and return true is thet are the same.

Overall last line means the if either left od the right subtree of the root tree is equal to the subroot tree we can return true.
this is tagged as easy but i think it should be medium
'''
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

        if not subRoot: return True
        if not root: return False
        if root.val == subRoot.val:
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
        