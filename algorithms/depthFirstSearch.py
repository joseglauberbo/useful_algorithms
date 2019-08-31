#coding: utf-8

from collections import defaultdict

class Graph:
	
	#inicializar o grafo
	def __init__(self): 
		self.graph = defaultdict(list) 
		
	#adicionando um vértice ao grafo
	def addEdge(self,u,v):
		self.graph[u].append(v)
	
	def DFSUtil(self, v, visited):
		
		#primeiro elemento a ser visitado no grafo na primeira chamada, dps da recursiva seria o filho
		visited[v] = True
		print v
		
		#como cada vértice tem um "array" de vertices conectados, verifica indo descendo quais já foram visitados
		for i in self.graph[v]:
			if (visited[i] == False):
				self.DFSUtil(i, visited)
		
	def DFS(self, v):
		
		#preenchendo o array de visitados com false
		visited = [False] * (len(self.graph))
		
		#primeiro vértice a ser visitado
		self.DFSUtil(v, visited)

#importante ressaltar que a ordem de impressão se dá pela ordem que foi adicionado
g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 3)
g.addEdge(2, 0) 
g.addEdge(3, 3)

g.DFS(0)
		
