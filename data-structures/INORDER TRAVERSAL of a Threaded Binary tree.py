#Inorder traversal of a threaded binary tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.right=None
        self.left=None
        self.threaded=0

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
            root.threaded=1

def left(root):
    if root:
        while root.left:
            root=root.left
        return root

def inorder_traversal(root):
    curr=left(root)
    while(1):
        print(curr.data)
        if curr.threaded==1:
            curr=curr.right
        else:
            curr=left(curr.right)
            print (curr)
            if curr==None:
                break


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
#print(root.left.right.right.data)#1
#print(root.left.left.right.right.data)#2
#print(root.left.left.right.left.right.data)#6

inorder_traversal(root)
