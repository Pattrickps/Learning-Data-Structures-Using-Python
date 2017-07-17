# convert a binary tree to a binary search tree
# maintain the same structure as that of the Binary tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def inorder_list(root):
    if root:
        inorder_list(root.left)
        q.append(root.data)
        inorder_list(root.right)

def convert(root):
    if root:
        convert(root.left)
        k=q.pop(0)
        root.data=k
        convert(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(40)
root.left.right=Node(20)
q=[]
inorder_list(root)
#print(q)
q.sort()
#print(q)
convert(root)
inorder(root)






