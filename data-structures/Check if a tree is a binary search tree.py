#check if a binary tree is a BST or not !

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.left=None
        self.right=None

def check(root,prev,boolval):
    if root.left:
        prev,boolval=check(root.left,prev,boolval)
    if boolval==True:
        if prev<root.data:
            prev=root.data
            if root.right:
                prev,boolval=check(root.right,prev,boolval)
            return prev,boolval
        else:
            return root.data,False

    else:
        return root.data,False


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

p,q=check(root,0,True)
if q==True:
    print("Yes this is BST")

else:
    print("no its not BST")




