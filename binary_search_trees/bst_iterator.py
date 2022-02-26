# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.root = root
        self.inorder_list = []
        self.iterator = -1
        self.inorder(self.root)
        
        
    def next(self) -> int:
        
        self.iterator += 1
        return self.inorder_list[self.iterator]
    
        
    def hasNext(self) -> bool:
        
        if self.iterator >= len(self.inorder_list)-1: return False
        else: return True
        
    
    def inorder(self,node):
        
        if node == None:
            return
        
        self.inorder(node.left)
        self.inorder_list.append(node.val)
        self.inorder(node.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()