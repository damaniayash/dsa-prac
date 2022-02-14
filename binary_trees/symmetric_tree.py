# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
   
    def preleft(self, root ,llist):
        if root == None:
            llist.append('null')
            return
        llist.append(root.val)
        self.preleft(root.left,llist)
        self.preleft(root.right,llist)
    
    def preright(self, root ,rlist):
        if root == None:
            rlist.append('null')
            return
        rlist.append(root.val)
        self.preright(root.right, rlist)
        self.preright(root.left, rlist)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        llist = [root.val]
        rlist = [root.val]
        self.preleft(root.left, llist)
        self.preright(root.right, rlist)
        # print(llist)
        # print(rlist)
        if llist == rlist:
            return True
        else:
            return False
        
        