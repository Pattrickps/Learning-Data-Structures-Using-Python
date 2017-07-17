# level wise insertion in a binary tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.right=None
        self.left=None

def insert(new_list):
    l=new_list
    q=[]
    k=l.pop(0)
    root_node=Node(k)
    q.append(root_node)

    while(len(l)>0):
        k=l.pop(0)
        m=q.pop(0)
        m.left=Node(k)
        q.append(m.left)
        if len(l)>0:
            k=l.pop(0)
            m.right=Node(k)
            q.append(m.right)

    return (root_node)


root_node=insert([1,2,3,4,5,6,7,8,9,10])
print(root_node.left.data)
print(root_node.right.left.data)
