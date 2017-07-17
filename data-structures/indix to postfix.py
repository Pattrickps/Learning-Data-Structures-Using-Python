# Infix to Postfix conversion

class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack)==0:
            print("sorry the stack is empty and u can't pop")
        else:
            i=self.stack.pop()
            #print("you poped out ",i)
        return(i)

    def peek(self):
        return (self.stack[-1])

    def printstack(self):
        print (self.stack,end=" ")

class infixtopostfix(Stack):
    def __init__(self,expression):
        Stack.__init__(self)
        self.result=[]
        self.p={}
        self.p["*"]=3
        self.p["/"]=3
        self.p["+"]=2
        self.p["-"]=2
        self.p["("]=1
        self.new_expression=expression.split()

    def convert(self):
        for token in self.new_expression:
            if token.isalpha():
                self.result.append(token)
            elif token=="(":
                self.push(token)

            elif token==")":
                while not self.peek()=="(":
                    k=self.pop()
                    self.result.append(k)
                self.pop()

            else:
                while len(self.stack)>0 and self.p[self.peek()]>=self.p[token]:
                    m=self.pop()
                    self.result.append(m)
                self.push(token)

    def printpostfix(self):
        while not len(self.stack)==0:
            k=self.pop()
            self.result.append(k)

        print(" ".join(self.result))

obj=infixtopostfix(" ( a + b ) * ( m + n ) ")
obj.convert()
obj.printpostfix()




