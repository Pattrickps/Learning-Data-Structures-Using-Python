# Graphs- DFS
from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.num_vertex=n
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS_HELP(self,v,visited):
        for i in self.graph[v]:
            if visited[i]==False:
                visited[i]=True
                print(i)
                self.DFS_HELP(i,visited)

    def DFS(self,root):
        visited=[False]*self.num_vertex
        visited[root]=True
        print(root)
        self.DFS_HELP(root,visited)

g = Graph(5)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 0)
g.addEdge(3, 0)
#g.addEdge(5, 4)
g.DFS(0)

