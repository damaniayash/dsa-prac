# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        if not l and r:
            return r
        if l and not r:
            return l
        elif r and l:
            return root
        else:
            return None
        
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         ppath, pans = [], []
#         qpath, qans = [], []
#         self.helperp(root, p, pans, ppath)
#         self.helperq(root, q, qans, qpath)
#         pans, qans = pans[0], qans[0]
#         for i in range(min(len(pans),len(qans))):
#             if pans[i].val == qans[i].val:
#                 lca = pans[i]
#         return lca
         
#     def helperp(self, node, p, pans, ppath):
#         if node == None:
#             return 
#         if node.val == p.val:
#             pans.append(ppath + [node])
#         self.helperp(node.left, p, pans, ppath = ppath + [node])
#         self.helperp(node.right, p, pans, ppath = ppath + [node])
    
#     def helperq(self, node, q, qans, qpath):
#         if node == None:
#             return 
#         if node.val == q.val:
#             qans.append(qpath + [node])
#         self.helperq(node.left, q, qans, qpath = qpath + [node])
#         self.helperq(node.right, q, qans, qpath = qpath + [node])
    
    
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         pstring, qstring = "",""
#         ppath, qpath = [], []
#         lca = 0
#         self.helperp(root, pstring, p, ppath)
#         self.helperq(root, qstring, q, qpath)
#         pp, qq = ppath[0], qpath[0]
#         ppath, qpath = pp.split(',') , qq.split(',')
#         print(ppath)
#         print(qpath) 
#         for i in range(0, min(len(qpath),len(ppath))):
#             if ppath[i] == qpath[i]:
#                 lca = int(ppath[i])
#         lcanode = []
#         self.nodefinder(root, lca, lcanode)
#         return (lcanode[0])
    
#     def nodefinder(self, node, lca, lcanode):
#         if node == None:
#             return
#         if node.val == lca:
#             lcanode.append(node)
#             return
#         self.nodefinder(node.left, lca, lcanode)
#         self.nodefinder(node.right, lca, lcanode)
        
#     def helperp(self, node, pstring, p, ppath):
#         if node == None:
#             return
#         if node.val == p.val:
#             ppath.append(pstring + str(node.val))
#         self.helperp(node.left, pstring+str(node.val)+",", p, ppath)
#         self.helperp(node.right, pstring+str(node.val)+",", p, ppath)
        
#     def helperq(self, node, qstring, q, qpath):
#         if node == None:
#             return
#         if node.val == q.val:
#             qpath.append(qstring + str(node.val))
#         self.helperq(node.left, qstring+str(node.val)+",", q, qpath)
#         self.helperq(node.right, qstring+str(node.val)+",", q, qpath)
        
        