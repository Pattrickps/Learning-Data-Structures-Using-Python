# sudo--where all the vertices cannot be reached from the root
from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.num_vertex=n
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def sudo_HELP(self,v,visited):
        visited[v]=True
        print(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.sudo_HELP(i,visited)

    def sudo(self):
        #length=len(self.graph)
        visited=[False]*self.num_vertex
        for i in list(range(self.num_vertex)):
            if visited[i]==False:
                self.sudo_HELP(i,visited)


g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 0)
g.addEdge(3, 0)
g.addEdge(5, 4)

print(g.graph)
g.sudo()
print (g.graph)
