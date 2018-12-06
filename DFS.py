# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:44:53 2018

@author: Fabricio

Depth First Search or DFS for a Graph

  
# This code is contributed by Neelam Yadav 
https://www.geeksforgeeks.or
"""
from collections import defaultdict

class Graph:
    #constructor
    def __init__(self):
        self.graph=defaultdict(list)
    
    # function to add an edge to graph 
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    # A function used by DFS 
    def DFSUtil(self,v,visited):
         # Mark the current node as visited and print it
        visited[v]=True
        print(v, end=' ')
        
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
    
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self,v):
         # Mark all the vertices as not visited
        visited=[False]*(len(self.graph))
        
        # Call the recursive helper function to print 
        # DFS traversal 
        self.DFSUtil(v,visited)

# Driver code 
# Create a graph 
g=Graph()        
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print('Following is DFS from (strarting from vertex 2)')

g.DFS(2)



