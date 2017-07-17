# Insertion in a binary search tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def insert(root,node):
    if node.data>root.data:
        if root.right==None:
            root.right=node
        else:
            insert(root.right,node)
    else:
        if root.left==None:
            root.left=node
        else:
            insert(root.left,node)

def inorder(root):
    if root:
        inorder(root.left)
        print (root.data)
        inorder(root.right)


root=Node(30)
insert(root,Node(20))
insert(root,Node(40))
insert(root,Node(35))
insert(root,Node(50))
insert(root,Node(60))

inorder(root)


