# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return 
        
        if root.val == key:
            
            if root == None or not root.left and not root.right:
                return None

            elif root.left and root.right:
                nextnode = self.inordersucc(root, key)
                _ , parent_inordersucc = self.search(root, nextnode.val) 

                if parent_inordersucc.left.val == nextnode.val:
                    parent_inordersucc.left = None

                elif parent_inordersucc.right.val == nextnode.val:
                    parent_inordersucc.right = None

                if root.val == parent_inordersucc.val:
                    nextnode.left = root.left
                elif nextnode.right:
                    nextnode.left = root.left
                    parent_inordersucc.left = nextnode.right
                    nextnode.right = root.right
                else:
                    nextnode.left = root.left
                    nextnode.right = root.right
                root = nextnode
                return root

            elif root.val == key:
                if root.left:
                    root = root.left
                elif root.right:
                    root = root.right
                return root
            
        elif not root.left and not root.right:
                return root   
            
        #parent is not null after this
        node , parent = self.search(root, key)
        if not node:
            return root
        # print('node to be deleted :',node.val)
        # print('parent :',parent.val)
        
        # leaf node (node with no children)
        if not node.left and not node.right:
            
            if parent.right and parent.right.val == key:
                parent.right = None
                
            elif parent.left and parent.left.val == key:
                parent.left = None
                
        #node with two children
        elif node.left and node.right:
            
            nextnode = self.inordersucc(root, key)
            _ , parent_inordersucc = self.search(root, nextnode.val) 
            
            if parent_inordersucc.left.val == nextnode.val:
                parent_inordersucc.left = None
                
            elif parent_inordersucc.right.val == nextnode.val:
                parent_inordersucc.right = None
                
            #successor is in right subtree
            if node.val == parent_inordersucc.val:
                nextnode.left = node.left
            elif nextnode.right:
                nextnode.left = node.left
                parent_inordersucc.left = nextnode.right
                nextnode.right = node.right
                
            else:
                nextnode.left = node.left
                nextnode.right = node.right
            
            if parent.left and parent.left.val == key:
                parent.left = nextnode
                
            elif parent.right and parent.right.val == key:
                parent.right = nextnode
                    
        #node with one child only
        else:
            if node.left:
                nextnode = node.left
                
            elif node.right:
                nextnode = node.right
                
            if parent.left and parent.left.val == key:
                parent.left = nextnode
                
            elif parent.right and parent.right.val == key:
                parent.right = nextnode
        
        return root
        
        
    def inordersucc(self, root, key):
        
        node , _ = self.search(root, key)
        if node.right:
            
            node = node.right
            while node.left:
                node = node.left
            return node
        
        else:
            
            ancestor = root
            successor = None
            
            while ancestor != node:
                
                if node.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.left
                    
                else:
                    ancestor = ancestor.right
            return succesor
        
        
    def search(self, node, key):
        
        parent = None   
        
        while node.val != key:
            
            parent = node
            #print(node.val)
            if not node.left and not node.right and node.val != key:
                return None, None
            elif node.left and node.val > key:
                node = node.left
                
            elif node.right and node.val < key:
                node = node.right
                
        return node , parent
            