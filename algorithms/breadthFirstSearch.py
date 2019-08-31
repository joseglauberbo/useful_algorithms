#coding: utf-8

from collections import defaultdict

class Graph:
	
	#inicializar o grafo
	def __init__(self): 
		self.graph = defaultdict(list) 
		
	#adicionando um vértice ao grafo
	def addEdge(self,u,v):
		self.graph[u].append(v)
		
	#metodo que faz a busca em largura no grafo sempre olhando os seus adjacentes
	#usa fila para facilitar e ter controle sobre o while, já q o laço se baseia nela para parar a execução
	def BFS(self, s):
		
		visited = [False] * len(self.graph)
		queue = []
		
		queue.append(s)
		visited[s] = True;
		
		while queue:
			
			s = queue.pop(0)
			print s
			
			for i in self.graph[s]:
				if (visited[i] == False):
					queue.append(i)
					visited[i] = True 
			
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)

g.BFS(2)
		
		
		
