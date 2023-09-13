# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
The idea is that preorder tells you which node are to be created first.
Inorder traversal tells you where the nodes are located wrt to each other.
Pop element from preorder array, find that element in the inorder array.
All the elemnts to the left of popped element in inorder array would be in the left subtree
    and those to the right are in the right subtree.
So during every call check if the preorder list is empty.
If not assign the node the value from preorder pop. The node is created and passed through the previous call.
if the left side of the current node is not empty
    first create a new node and attach it to the left of current node.
    call construct on this newly created node with only the left side of inorder.
do the same thing for right side as well.
return node
'''
class Solution:
    class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def construct(node, preorder, inorder):

            if not preorder:
                return

            node.val = preorder.pop(0)
            index = inorder.index(node.val)

            if inorder[0:index]:
                node.left = TreeNode()
                construct(node.left, preorder, inorder[0:index])
            
            if inorder[index+1:]:
                node.right = TreeNode()
                construct(node.right, preorder, inorder[index+1:])
            
            return node
        
        root = TreeNode()
        return construct(root, preorder, inorder)

