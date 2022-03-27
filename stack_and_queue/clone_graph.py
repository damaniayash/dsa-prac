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
        visited, node_dict = [], {}
        #node_dict contains original node as key and new node as value.
        new_node = Node(node.val)
        self.helper(node,visited,new_node,node_dict)
        return new_node
        
    def helper(self,node,visited,new_node,node_dict):
        visited.append(node)
        node_dict[node] = new_node
        for i in node.neighbors:
            if i in visited:
                new_node.neighbors.append(node_dict[i])
                continue 
            else: #i is not encountered before
                temp = Node(i.val)
                new_node.neighbors.append(temp)
                self.helper(i,visited,temp,node_dict) 
                    
        
        