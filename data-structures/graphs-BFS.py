# graphs- BFS

from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.graph = defaultdict(list)
        self.num_vertex=n
        
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,s):
        visited=[False]*self.num_vertex
        q=[]
        q.append(s)
        visited[s]=True
        print(s)
        while(1):
            v=q.pop(0)
            
            for i in self.graph[v]:
                #print("for i = %d" %(i))
                if visited[i]==False:
                    q.append(i)
                    visited[i]=True
                    print(i)
            if len(q)==0:
                break
            
                    


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 0)
g.addEdge(3, 0)

g.bfs(0)

print(g.graph)
