"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    def serialize(self, root: DirectedGraphNode):

        if not root:
            return '#0'
        queue = [root]
        encoded = [str(root.label)]

        while queue:
            node = queue.pop(0)
            num_child = len(node.neighbors)
            encoded.append('#' + str(num_child))
            if node.neighbors:
                for child in node.neighbors:
                    queue.append(child)
                    encoded.append(str(child.label))
            else:
                encoded.append('#0')
        print(encoded)
        return encoded


    def deserialize(self, data: str):
        
        if data == '#0':
            return None
        
        root = DirectedGraphNode(int(data[0]))
        queue = [root]

        i = 1
        while queue:
            _, child_len = data[i]
            node = queue.pop(0)

            for j in range(int(child_len)):
                child_node = DirectedGraphNode(int(data[i+j+1]))
                node.neighbors.append(child_node)
                queue.append(child_node)
            
            i += int(child_len) + 1

        return root




# # lINTCODE


# """
# Definition for a directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
# """


# class Solution:
#     def serialize(self, root: DirectedGraphNode):
#         if root == None:
#             return '#'
#         ans = []
#         queue = [root]
#         ans = [str(root.label)]
#         while queue:
#             node = queue.pop(0)
#             #print('node:', node.label, node.neighbors)
#             ans.append('#' + str(len(node.neighbors)))
#             if node.neighbors:
#                 for n in node.neighbors:
#                     queue.append(n)
#                     ans.append(str(n.label))
#             else:
#                 ans.append('#0')
        
#         #print(ans)
#         return ans
            

#     def deserialize(self, data: str):
#         if data == '#':
#             return None
#         print('deser', data)
#         root = DirectedGraphNode(int(data[0]))
#         queue = [root]

#         i = 1
#         while queue:
#             node = queue.pop(0)
#             chlen = int(data[i][1:])
#             print(int(chlen))
#             for j in range(0, int(chlen)):
#                 chnode = DirectedGraphNode(int(data[i+j+1]))
#                 node.neighbors.append(chnode)
#                 queue.append(chnode)
#             i += int(chlen) + 1
        
#         return root





