#Queue Data Structure

class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue)==0:
            print("sorry the queue is empty")
        else:
            i=self.queue.pop(0)
            print("you dequeued out ",i)

    def front(self):
        print (self.queue[0])
        print("\n")

    def rear(self):
        print (self.queue[-1])
        print("\n")

    def printqueue(self):
        print (self.queue,end=" ")
        

obj=queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)

obj.printqueue()
obj.dequeue()
obj.printqueue()

obj.rear()
obj.front()










        
