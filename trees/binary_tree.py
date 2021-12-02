class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self,root):
        self.root = root

node = Node(10)
node.left = Node(5)
node.right = Node(15)
node.left.left = Node(2)
node.left.right = Node(7)
node.right.left = Node(12)
node.right.right = Node(100)
print(node.right.data)

'''
        10
    5       15
2     7   12    100
'''