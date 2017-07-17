#Singly Linked List- Insert a new node after a given node

class Node:
    def __init__(self,node_data):
        self.data=node_data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def Push(self,node_data):
        new_node=Node(node_data)
        new_node.next=self.head
        self.head=new_node

    def append(self,node_data):
        new_node=Node(node_data)
        last=self.head
        while(1):
            if last.next==None:
                last.next=new_node
                break
            last=last.next

    def insertafter(self,prevnode,node_data):
        new_node=Node(node_data)
        new_node.next=prevnode.next
        prevnode.next=new_node

    def printlist(self):
        l=self.head
        while(1):
            if l==None:
                break
            print (l.data,end=" ")
            l=l.next

obj=Linkedlist()
obj.Push(1)
obj.Push(2)
obj.Push(3)
obj.printlist()
print("\n")
obj.append(4)
obj.printlist()
print("\n")
obj.insertafter(obj.head,5)
obj.printlist()

            
