# STACKS

class stack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack)==0:
            print("sorry the stack is empty and u can't pop")
        else:
            i=self.stack.pop()
            print("you poped out ",i)

    def peek(self):
        print (self.stack[-1])

    def printstack(self):
        print (self.stack,end=" ")

obj=stack()
obj.push(1)
obj.push(2)
obj.push(3)

obj.printstack()
print("\n")
obj.pop()
obj.printstack()
