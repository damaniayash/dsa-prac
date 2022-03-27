"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        visited = []
        node_dict = {}
        new_node = Node(node.val)
        self.helper(node,visited,new_node,node_dict)
        # for k, v in node_dict.items():
        #     print(k,v)
        #     print(k.val, v.val)
        return new_node
        
    def helper(self,node,visited,new_node,node_dict):
        #print(node.val)
        visited.append(node)
        curr_node = new_node
        node_dict[node] = curr_node
        #[print('vis',i.val) for i in visited]
        for i in node.neighbors:
            if i in visited:
                curr_node.neighbors.append(node_dict[i])
                continue 
            else: #i is not encountered before
                temp = Node(i.val)
                curr_node.neighbors.append(temp)
                #temp.neighbors.append(curr_node)
                self.helper(i,visited,temp,node_dict) 
                    
        
        