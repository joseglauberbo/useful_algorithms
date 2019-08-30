#coding:utf-8

lista = [21,23,2,34,245,245,0,33,66]

#função de troca in-place
def swap(list,a,b):
	temp = list[a]
	list[a] = list[b]
	list[b] = temp
	
#adota um pivot e vai verificando sempre com o proximo se está ordenado. Pior caso: O(n²). Melhor Caso: O(n).
def gnomeSort(lista):
	pivot = 0
	
	while (pivot < (len(lista) - 1)):
		if (lista[pivot] <= lista[pivot+1]):
			pivot += 1
		else: 
			swap(lista, pivot, pivot+1)
			if (pivot == 0):
				pivot += 1
			if (pivot == (len(lista) - 1)):
				break
			else: 
				pivot -= 1 
	return lista

print gnomeSort(lista)
