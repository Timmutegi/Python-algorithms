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

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def traversePreorder(self):
        self.root.traversePreorder()

    def traverseinorder(self):
        self.root.traverseInorder()

    def traversePostorder(self):
        self.root.traversePostorder()


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