#Linked List- Delete duplicates WITHOUT using a Hash table

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

    def deletedup(self):
        length=0
        l=self.head
        while(1):
            length+=1
            l=l.next
            if l==None:
                break

        table=[]
        for i in list(range(length)):
            table.append([])

        l=self.head
        while(l):
            key=l.data % length
            if table[key]!=l.data:
                table[key]=l.data
                prev=l
                l=l.next

            else:
                prev.next=l.next
                l=l.next
            print (table)
    def deleteduprunner(self):
        current=self.head
        while(current):
            runner=current
            while(runner.next):
                if runner.next.data==current.data:
                    runner.next=runner.next.next
                else:
                    runner=runner.next
            current=current.next

obj=Linkedlist()
obj.Push(1)
obj.Push(3)
obj.Push(3)
obj.append(4)
obj.printlist()
print("\n")
obj.deleteduprunner()
print("\n")
obj.printlist()



            
