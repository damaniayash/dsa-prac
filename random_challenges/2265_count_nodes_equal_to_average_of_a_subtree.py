# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        inorder_list = []
        self.inorder(root, inorder_list)
        count = 0
        for i in inorder_list:
            temp = []
            self.inorder_val(i,temp)
            #print(i.val,'---',temp)
            if sum(temp)//len(temp) == i.val:
                #print(sum(temp)//len(temp),i.val)
                count += 1
        return count
    
    def inorder(self, node, inorder_list):
        if not node:
            return
        self.inorder(node.left, inorder_list)
        inorder_list.append(node)
        self.inorder(node.right, inorder_list)
    
    def inorder_val(self, node, inorder_list):
        if not node:
            return
        self.inorder_val(node.left, inorder_list)
        inorder_list.append(node.val)
        self.inorder_val(node.right, inorder_list)