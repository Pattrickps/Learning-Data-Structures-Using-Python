# Level order traversal in a binary tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def TRAVERSE(root):
    q=[]
    if root:
        print (root.data)
        q.append(root)

    while len(q)>0:
        current=q.pop(0)
        if current.left:
            print (current.left.data)
            q.append(current.left)

        if current.right:
            print(current.right.data)
            q.append(current.right)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
TRAVERSE(root)
