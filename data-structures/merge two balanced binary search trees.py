#merge two Balanced Binary search tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.right=None
        self.left=None

def inorder_list(root):
    if root:
        inorder_list(root.left)
        q.append(root.data)
        inorder_list(root.right)

def convert(l):
    if len(l)>0:
        mid_index=int(len(l)/2)
        mid=l[mid_index]
        new_node=Node(mid)
        l2=l[0:mid_index]
        new_node.left=convert(l2)
        if len(l)>2:
            l3=l[mid_index + 1:]
            new_node.right=convert(l3)
            return new_node
        return new_node

    else:
        return None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)



root1 = Node(50)
root1.left = Node(30)
root1.right = Node(70)
root1.left.left = Node(20)
root1.left.right = Node(40)
root1.right.left = Node(60)
root1.right.right = Node(80)


root2 = Node(100)
root2.left = Node(90)
root2.right = Node(120)
root2.left.left = Node(75)
root2.left.right = Node(95)
root2.right.left = Node(115)
root2.right.right = Node(130)
q=[]
inorder_list(root1)
inorder_list(root2)
q.sort()

root=convert(q)
inorder(root)


