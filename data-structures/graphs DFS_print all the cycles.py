# Graphs DFS--will print all the present cycles
from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.num_vertex=n
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS_HELP(self,v,visited,q):
        for i in self.graph[v]:
            if visited[i]==False:
                visited[i]=True
                #print(i)
                q.append(i)
                #print(q)
                self.DFS_HELP(i,visited,q)
                q.pop(-1)
            else:
                #print(i)
                if i in q:
                    print("there is a cyle from %d to %d" %(v,i))
        

    def DFS(self,root):
        q=[]
        visited=[False]*self.num_vertex
        visited[root]=True
        #print(root)
        q.append(root)
        self.DFS_HELP(root,visited,q)
                


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 0)
g.addEdge(3, 0)
g.DFS(0)
