# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:02:04 2018

@author: Fabricio

Breadth First Search for a graph

# This code is contributed by Neelam Yadav 
https://www.geeksforgeeks.or
"""
from collections import defaultdict

class Graph:
    #construsctor
    def __init__(self):
        #diccionario por defecto para almacenar gráfico
        self.graph = defaultdict(list)
        
        #funcion para agregar un edge al grafico
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
        #funcion para imprimir un BFS del grafico
    def BFS(self, s):
        #marcar todos los vertices como no visitados
        visited = [False] * (len(self.graph))
        
        #create una cola para el BFS
        queue = []
        
        #marcar el nodo original como visitado
        #y ponerlo en cola
        queue.append(s)
        visited[s]=True
        
        while queue:
            #sacar de la cola un vertice de la
            #cola e imprimirlo
            s=queue.pop(0)
            print(s, end=' ')
            
        #obtener todos los vertices adyacentes 
        #del vertice s en la cola. si uno de los 
        #vertices no fue visitado, marcarlo como visitado
        #y ponerlo en la ola
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
                    
#driver code
#crear un gráfico
g=Graph()                 
g.addEdge(0,1)   
g.addEdge(0,2)   
g.addEdge(1,2)   
g.addEdge(2,0)   
g.addEdge(2,3)   
g.addEdge(3,3)   

print('Following is Breadth First Traversal'  '(starting from vertex 2)')

g.BFS(2)























