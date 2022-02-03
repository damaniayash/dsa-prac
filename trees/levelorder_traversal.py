# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        level = [root]
        while root and level:
            currentNodes = []
            nextLevel = []
            for node in level:
                currentNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ret.append(currentNodes)
            level = nextLevel
        return ret
        # if root == None:
        #     return
        # que = []
        # res = []
        # que.append(root)
        # res.append([root.val])
        # temp = []
        # #print(que[0].data)
        # while que: #list not empty
        #     #print("Node data - ",que[0].val)
        #     if que[0].left != None:
        #         que.append(que[0].left)
        #         temp.append(que[0].left.val)
        #     if que[0].right != None:
        #         que.append(que[0].right)
        #         temp.append(que[0].right.val)
        #     if temp:
        #         res.append(temp)
        #     temp = []
        #     que.pop(0)
        # return res
        