# Implement Stack using Linked List

class node:
    def __init__(self,node_data):
        self.data=node_data
        self.next=None

class stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def pop(self):
        if self.head==None:
            print("sorry the stack is empty")

        else:
            print("the poped element is", self.head.data)
            self.head=self.head.next

    def peek(self):
        print(self.head.data)

    def printstack(self):
        l=self.head
        while(1):
            if l==None:
                break
            print (l.data,end=" ")
            l=l.next

obj=stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.printstack()
print("\n")
obj.pop()
print("\n")

obj.printstack()
            


