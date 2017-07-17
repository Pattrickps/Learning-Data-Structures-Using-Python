# Height of a Binary tree / Binary search tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def height_tree(root):
    if root==None:
        return 0
    h1=height_tree(root.left)
    h2=height_tree(root.right)

    if h1>h2:
        height=h1
        return height+1

    else:
        height=h2
        return height+1



root=Node(50)
root.left=Node(30)
root.right=Node(60)
root.left.left=Node(20)
root.left.right=Node(40)
h=height_tree(root)
print(h-1)


