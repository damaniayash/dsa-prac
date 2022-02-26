from statistics import mode


class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def __init__(self,root):
        self.root = root
        self.temp = []

    def search(self,target):
        if self.root.data == target:
            return self.root.data
        if self.root.left != None and target < self.root.data:
            self.root.left.search(target)
        if self.root.right != None and target > self.root.data:
            self.root.right.search(target)

    def inorder_successor(self, root, targetval):
        if self.root == None:
            return
        node = self.root
        while node.data != targetval:
            print(node.data)
            if node.left != None and targetval < node.data:
                node = node.left
            elif node.right != None and targetval > node.data:
                node = node.right
        print('currently at : ', node.data)
        if node.right != None:
            node = node.right
            while node.left != None:
                node = node.left
            print('right subtree present, successor is',node.data)
        else:
            ancestor = self.root
            while ancestor != node:
                if node.data < ancestor.data:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            print('right subtree not present, successor is', successor.data)




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

    def post_order(self,root):
        if root == None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data)

    def level_order(self, root):
        que = []
        que.append(root)
        #print(que[0].data)
        while que: #list not empty
            print("Node data - ",que[0].data)
            #que.pop(0)
            if que[0].left != None:
                que.append(que[0].left)
            if que[0].right != None:
                que.append(que[0].right)
            que.pop(0)

    def levelOrder(self, root):
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
    
    def level_order_lc(self, root):
        que = []
        res = []
        que.append(root)
        res.append([root.data])
        temp = []
        c = 0
        #print(que[0].data)
        while que: #list not empty
            print("Node data - ",que[0].data)
            if que[0].left != None:
                que.append(que[0].left)
                temp.append(que[0].left.data)
            if que[0].right != None:
                que.append(que[0].right)
                temp.append(que[0].right.data)
            if temp:
                res.append(temp)
            temp = []
            que.pop(0)
        return res

           
# node = Node(10)
# node.left = Node(5)
# node.right = Node(15)
# node.left.left = Node(2)
# node.left.right = Node(7)
# node.right.left = Node(12)
# node.right.right = Node(100)

node = Node(15)
node.left = Node(10)
node.right = Node(20)
node.left.left = Node(8)
node.left.right = Node(12)
node.right.left = Node(17)
node.right.right = Node(25)
node.left.left.left = Node(6)
node.left.right.left = Node(11)
node.right.left.left = Node(16)
node.right.right.right = Node(27)

tree = Tree(node)

#Search
# ans = tree.search(10)
# if ans:
#     print(f"Value found : {ans}")

# #Traversal
# print("Pre-order : ")
# tree.pre_order(node)
# print("In-order : ")
# tree.in_order(node)
# print("Post-order : ")
# tree.post_order(node)

#tree.level_order(node)
#print(tree.level_order_lc(node))
tree.inorder_successor(node, 17)

'''
        10
    5       15
2     7   12    100
'''
