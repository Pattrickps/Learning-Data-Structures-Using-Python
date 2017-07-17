# sorted array to binary search tree

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def convert(l):
    if len(l)>0:
        mid_index=int(len(l)/2)
        mid=l[mid_index]
        root_node=Node(mid)
        l2=l[0:mid_index]
        root_node.left=convert(l2)
        if len(l)>2:
            l3=l[mid_index+1:]
            root_node.right=convert(l3)
        return root_node

    else:
        return None




root=convert([10,20,30,40,50,60])
print(root.left.right.data)
