#coding:utf-8

lista = [21,23,2,34,245,245,33,66]

#algoritmo que insere na ordem certa e faz isso pela chave. Pior caso: O(n²). Melhor Caso: O(n).
def insertionSort(lista):
	for i in range(1, len(lista)):
		key = lista[i]
		k = i
		while (k > 0 and key < lista[k-1]):
			lista[k] = lista[k-1]
			k = k - 1 
		lista[k] = key
	return lista

print insertionSort(lista)
	
