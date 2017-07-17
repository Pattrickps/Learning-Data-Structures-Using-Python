# Detecting cycles in an undirected graph using "stack of iterators"
from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.num_vertex=n
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def stack_of_iterator(self):
        visited=[False]*self.num_vertex
        stack=[iter(list(range(self.num_vertex)))]
        R_S=[]
        while stack:
            for i in stack[-1]:
                print("i is ",i)
                if visited[i]==False:
                    print(i)
                    visited[i]=True
                    R_S.append(i)
                    stack.append(iter(self.graph[i]))
                    
                elif i in R_S and i!=R_S[-2]:
                    print("cycle in the path from %d to %d" %(R_S[-1],i))
                break
            
            else:
                stack.pop()
                if len(R_S)>0:
                    k=R_S.pop()
                    print("popped %d" %(k))
                  

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.stack_of_iterator()
print (g.graph)
