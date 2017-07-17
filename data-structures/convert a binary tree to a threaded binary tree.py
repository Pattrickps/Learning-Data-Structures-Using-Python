#converting a binary tree to a threaded binary tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.right=None
        self.left=None

def inorderqueue(root):
    if root:
        inorderqueue(root.left)
        q.append(root)
        inorderqueue(root.right)

def convert(root):
    if root:
        convert(root.left)
        q.pop(0)
        convert(root.right)

        if root.right is None and len(q)>0:
            root.right=q[0]


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.right=Node(6)
root.left.left.right.left=Node(7)
q=[]
inorderqueue(root)
convert(root)
print(root.left.right.right.data)#1
print(root.left.left.right.right.data)#2
print(root.left.left.right.left.right.data)#6
