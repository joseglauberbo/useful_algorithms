#coding:utf-8

lista = [21,23,2,34,245,33,66]

#função de troca in-place
def swap(list,a,b):
	temp = list[a]
	list[a] = list[b]
	list[b] = temp
	
#ALGORITMOS ITERATIVOS
	
#algoritmo que leva o item de maior valor para o final da lista. Pior caso: O(n²). Melhor Caso: O(n²).
def bubbleSort(lista):
	
	for i in range(len(lista)):
		for j in range(len(lista)-1):
			if (lista[j]>lista[j+1]):
				swap(lista, j, j+1)
	return lista

print bubbleSort(lista)
