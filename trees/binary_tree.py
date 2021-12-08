class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self,root):
        self.root = root

    def search(self,target):
        if self.root.data == target:
            return self.root.data
        if self.root.left != None and target < self.root.data:
            self.root.left.search(target)
        if self.root.right != None and target > self.root.data:
            self.root.right.search(target)

    def pre_order(self,root):
        if root == None:
            return
        print(root.data)
        self.pre_order(root.left)
        self.pre_order(root.right)
    
    def in_order(self,root):
        if root == None:
            return 
        self.in_order(root.left)
        print(root.data)
        self.in_order(root.right)
    
    

        


node = Node(10)
node.left = Node(5)
node.right = Node(15)
node.left.left = Node(2)
node.left.right = Node(7)
node.right.left = Node(12)
node.right.right = Node(100)

tree = Tree(node)

#Search
ans = tree.search(10)
if ans:
    print(f"Value found : {ans}")

#Traversal
#print("Pre-order : ")
#tree.pre_order(node)
print("In-order : ")
tree.in_order(node)

'''
        10
    5       15
2     7   12    100
'''