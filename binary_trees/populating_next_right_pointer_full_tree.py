"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        res = []
        level = [root]
        while level:
            nextlevel = []
            currnodes = []
            for i in level:
                currnodes.append(i.val)
                if i.left != None:
                    nextlevel.append(i.left)
                if i.right != None:
                    nextlevel.append(i.right)
                    
            if len(level) == 1:
                level[0].next == None
                
            for i in range(0,len(level)-1):
                level[i].next = level[i+1]
                
            level[-1].next = None
            level = nextlevel
            
        return root
    
    
        # if not root:
        #     return
        # res = []
        # level = [root]
        # while level:
        #     nextlevel = []
        #     currnodes = []
        #     for i in level:
        #         currnodes.append(i.val)
        #         if i.left != None:
        #             nextlevel.append(i.left)
        #         if i.right != None:
        #             nextlevel.append(i.right)
        #     res.append(currnodes)
        #     level = nextlevel
        # print(res)
            
            
        