# POSTORDER TRAVERSAL IN A BINARY TREE

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

postorder(root)
