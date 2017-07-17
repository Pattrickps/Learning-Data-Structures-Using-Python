#Implement Queue using Linked List

class node:
    def __init__(self,node_data):
        self.data=node_data
        self.next=None

class queue:
    def __init__(self):
        self.head=None

    def enqueue(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def dequeue(self):
        if self.head==None:
            print("sorry the queue is empty")
        else:
            l=self.head
            while(1):
                if l.next==None:
                    p.next=None
                    break
                p=l
                l=l.next
            print("you dequeued out ",l.data)

    def front(self):
        print ("the front is ",self.head.data)
        print("\n")

    def rear(self):
        l=self.head
        while(1):
            if l.next==None:
                print("the rear is ",l.data)
                break
            l=l.next
        print("\n")

    def printqueue(self):
        l=self.head
        while(1):
            print(l.data,end=" ")
            if l.next==None:
                break
            l=l.next
        print("\n")

obj=queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)

obj.printqueue()
obj.dequeue()
obj.printqueue()





    










        






            
