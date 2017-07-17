# searching in a binary search tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def search(root,node):
    if root:
        if root.data==node.data:
            return node
        elif node.data>root.data:
            return search(root.right,node)
        else:
            return search(root.left,node)

    else:
        return root

root=Node(8)
root.right=Node(10)
root.left=Node(3)
root.right.right=Node(14)
root.left.left=Node(1)
root.left.right=Node(6)
root.left.right.left=Node(4)
root.left.right.right=Node(7)

print(search(root,Node(15)))


