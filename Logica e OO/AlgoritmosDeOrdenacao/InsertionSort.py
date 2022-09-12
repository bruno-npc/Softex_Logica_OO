#Faça um algoritmo de ordenação utilizando o método insertion sort.
#Crie um método que execute as seguintes operações:

#- Tamanho do vetor: 30;
#- Utilize números ímpares;
#- Opere em ordem crescente.

from random import *

def InsertionSort(lista):
    for i in range (0, len(lista)):
        atual = lista[i]

        while i > 0 and lista[i - 1] > atual:
            lista[i] = lista[i - 1]
            i -= 1
        
        lista[i] = atual


lista = [1] * 30
i = 0
impar = 1

while i < 30: 
    lista[i] = impar
    i += 1
    impar += 2

listaSorted = sorted(lista, reverse=True)
print(listaSorted)

InsertionSort(listaSorted)
print("\n\n", listaSorted, "\n\n")