# Tree traversals in a binary tree- A)INORDER TRAVERSAL
class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print (root.data)
        inorder(root.right)



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

inorder(root)
