# Inorder Traversal without recursion (using Stack)

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def inorder(root):
    s=[]
    if root:
        s.append(root)
    curr=root.left
    while(1):
        if curr:
            s.append(curr)
            curr=curr.left

        else:
            if len(s)>0:
                curr=s.pop()
                print(curr.data)
                curr=curr.right
            else:
                break


    

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.right=Node(6)
root.left.left.right.left=Node(7)
inorder(root)
