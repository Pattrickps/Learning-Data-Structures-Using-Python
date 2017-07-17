# Detecting cycles in a directed graph using "stack of iterators"
from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.num_vertex=n
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def stack_of_iterator(self):
        visited=[False]*self.num_vertex
        stack=[iter(list(range(self.num_vertex)))]
        R_S=[]
        while stack:
            for i in stack[-1]:
                if visited[i]==False:
                    print(i)
                    visited[i]=True
                    R_S.append(i)
                    stack.append(iter(self.graph[i]))
                    
                elif i in R_S:
                    print("cycle from %d to %d" %(R_S[-1],i))
                break
            
            else:
                stack.pop()
                if len(R_S)>0:
                    k=R_S.pop()
                    print("popped %d" %(k))
                  

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 0)
g.addEdge(3, 0)
g.stack_of_iterator()
