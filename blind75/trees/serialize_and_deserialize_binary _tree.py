
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        ans = []
        while queue:
            node = queue.pop(0)
            if node == None:
                ans.append('#')
            else:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(ans)
 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def createnode(strval):
            if strval == '#':
                return None
            else:
                return TreeNode(val=strval)

        if data == '#':
            return None
        print(data)
        data = data.split(',')
        root = createnode(data[0])
        queue = [root]

        i = 1
        while queue:
            node = queue.pop(0)
            node.left = createnode(data[i])
            node.right = createnode(data[i+1])

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            i += 2

        return root
            
              

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

## Does not work of test case
#[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if root == None:
            return ''

        queue = [[root]]
        ans = str(root.val) + '#' 

        while queue:
            level = queue.pop()
            next_level = []
            next_level_val = ''
            for node in level:
                if node.left:
                    next_level.append(node.left)
                    next_level_val += str(node.left.val) + ','
                else:
                    next_level_val += 'N,'

                if node.right:
                    next_level.append(node.right)
                    next_level_val += str(node.right.val) + ','
                else:
                    next_level_val += 'N,'
    
            if next_level:
                level = next_level
                queue.append(next_level)
                ans += next_level_val + '#'           
            
        print(ans)
        return ans

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if data == '':
            return 

        data = data.split('#')
        print(data)   
        for i in range(0, len(data)):
            elements = [x.strip() for x in data[i].split(',') if x.strip()]

            # Convert 'N' to None and other elements to integers
            result_list = [None if element == 'N' else int(element) for element in elements]
            data[i] = result_list
        data = data[:-1]
        data.append([[None] * 2 * len(data[-1])])
        print(data[-1])
        
        print(data) 

        queue = []
        root = TreeNode(val = data[0][0])
        queue.append(root)

        for i in range(len(data) - 1):
            j = 0
            while j+1 < len(data[i+1]):
                node = queue.pop(0)
                print(i, data[i], j)
                if data[i+1][j]:
                    left_node = TreeNode(val = data[i+1][j])
                    queue.append(left_node)
                    node.left = left_node

                if data[i+1][j+1]:
                    right_node = TreeNode(val = data[i+1][j+1])
                    queue.append(right_node)
                    node.right = right_node
                j += 2
        
        return root
            
                
                
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))