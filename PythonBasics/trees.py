"""
This class implements the tree data structure
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not in tree")

    def height(self, h = 0):
        leftHeight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)

    """
    Visit the nodes starting from the root then going to the left as much as you can
    """
    def traversePreorder(self):
        print(self.data)

        if self.left:
            self.left.traversePreorder()

        if self.right:
            self.right.traversePreorder()
    
    """
    Start with the smallest node then go left to right
    Start with the smallest node then go to the largest node in order
    """
    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()

        print(self.data)

        if self.right:
            self.right.traverseInorder()
    
    """
    Start with the left most node to the right visiting the root last
    """
    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()

        if self.right:
            self.right.traversePostorder()

        print(self.data)

    """
    Get the number of nodes at a given depth
    """
    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes

    """
    Add a node
    """
    def add(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                return
            else:
                self.left.add(data)
        
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
                return
            else:
                self.right.add(data)

class Tree:
    def __init__(self, root, name = ''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def height(self):
        return self.root.height()

    def traversePreorder(self):
        self.root.traversePreorder()

    def traverseinorder(self):
        self.root.traverseInorder()

    def traversePostorder(self):
        self.root.traversePostorder()

    def add(self, data):
        self.root.add(data)

    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodesAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')


node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(100)

myTree = Tree(node, 'Tim\'s Tree')

print(myTree.name)
print(myTree.root.left.data)

print(myTree.root.right.right.data)

found = myTree.search(100)
print(found.data)

print("Preorder Traversal")
myTree.traversePreorder()

print("Inorder Traversal")
myTree.traverseinorder()

print("Postorder Traversal")
myTree.traversePostorder()

print("Tree height:")
print(myTree.height())

myTree.print()

print("Adding a node")
myTree.add(50)

myTree.print()