"""
Given a binary tree root, check if it's symmetric around it's center (a mirror of itself)
"""

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def are_symmetric(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif ((root1 is None) != (root2 is None)) or (root1.val != root2.val):
            return False
        else:
            return self.are_symmetric(root1.left, root2.right) and self.are_symmetric(root1.right, root2.left)
            
    def is_assymetric(self, root):
        if root is None:
            return True
        return self.are_symmetric(root.left, root.right)                            

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(Solution().is_assymetric(root))
