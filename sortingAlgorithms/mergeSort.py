#coding: utf-8

lista = [21,23,2,34,245,33,66]

#algoritmo que faz divisão por conquista. Vai dividindo e depois juntando as partes já ordenadas
def first(lista):
	return lista[0]

def mergeSort(lista):
	
	meio = len(lista)/2

	if (len(lista) == 1):
		return lista

	return merge(mergeSort(lista[:meio]), mergeSort(lista[meio:]))
		
def merge(listaLeft, listaRight):
	result = []
	while (len(listaLeft) > 0 and len(listaRight) > 0):
		if (first(listaLeft) < first(listaRight)):
			result.append(first(listaLeft))
			listaLeft.remove(first(listaLeft))
		else:
			result.append(first(listaRight))
			listaRight.remove(first(listaRight))
	if (listaLeft > 0):
		result.append(listaLeft)
	else:
		result.append(listaRight)
	return result 

print mergeSort(lista)
