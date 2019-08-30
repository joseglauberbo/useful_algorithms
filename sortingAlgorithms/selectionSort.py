#coding:utf-8

lista = [21,23,2,34,245,33,66]

#função de troca in-place
def swap(list,a,b):
	temp = list[a]
	list[a] = list[b]
	list[b] = temp
	
#algoritmo que encontra o menor elemento da lista e aí leva ele pra a primeira posição. Pior caso: O(n²). Melhor Caso: O(n²).
def selectionSort(lista):
	for i in range(len(lista)):
		min = i
		for j in range(i, len(lista)):
			if (lista[j] < lista[min]):
				min = j
		swap(lista, i, min)
	return lista
	
print selectionSort(lista)
