# Preorder Traversal in a binary tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def preorder(root):
    if root:
        print (root.data)
        preorder(root.left)
        preorder(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

preorder(root)
